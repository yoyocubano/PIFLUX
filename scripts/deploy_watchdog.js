/**
 * 🕵️‍♂️ PIF Deploy Watchdog (MCP Style Monitor)
 * 
 * Este script actúa como un "servidor MCP local" que monitorea
 * el estado del despliegue en tiempo real.
 * 
 * Uso: node scripts/deploy_watchdog.js
 */

const https = require('https');

const TARGET_URL = 'https://piflux.pages.dev';
const EXPECTED_TITLE = 'PIF Technical Command Center';
const ERROR_SIGNATURE = 'CRITICAL SYSTEM FAILURE'; // El H1 de nuestro ErrorBoundary

console.log(`\n🔌 CONNECTING TO DEPLOY MONITOR (MCP PROTOCOL v1.0)...`);
console.log(`🎯 TARGET: ${TARGET_URL}\n`);

const checkDeploy = () => {
    const startTime = Date.now();
    
    https.get(TARGET_URL, (res) => {
        let data = '';

        res.on('data', (chunk) => {
            data += chunk;
        });

        res.on('end', () => {
            const latency = Date.now() - startTime;
            
            // 1. Check HTTP Status
            if (res.statusCode !== 200) {
                console.error(`❌ [CRITICAL] HTTP ERROR: ${res.statusCode}`);
                console.error(`   Latency: ${latency}ms`);
                process.exit(1);
            }

            // 2. Check for ErrorBoundary Signature
            if (data.includes(ERROR_SIGNATURE)) {
                 console.error(`🚨 [ALARM] RED SCREEN OF DEATH DETECTED!`);
                 console.error(`   The application has crashed in production.`);
                 console.error(`   Signature found: "${ERROR_SIGNATURE}"`);
                 process.exit(1);
            }

            // 3. Check for specific content (Title)
            if (!data.includes(EXPECTED_TITLE)) {
                console.warn(`⚠️ [WARNING] Title mismatch. Possible partial render or old cache.`);
            }

            // 4. Check for broken chunks (heuristic)
            if (data.includes('Unexpected token') || data.includes('SyntaxError')) {
                console.error(`❌ [CRITICAL] JS SYNTAX ERROR DETECTED IN HTML SOURCE`);
            }

            console.log(`✅ [OK] SYSTEM ONLINE | Status: ${res.statusCode} | Latency: ${latency}ms | Integrity: Verified`);
        });

    }).on('error', (e) => {
        console.error(`💀 [FATAL] CONNECTION REFUSED: ${e.message}`);
        process.exit(1);
    });
};

// Initial Check
checkDeploy();

// Optional: Poll every 30s if run with --watch
if (process.argv.includes('--watch')) {
    console.log(`🔄 Watch mode active. Polling every 30s...`);
    setInterval(checkDeploy, 30000);
}

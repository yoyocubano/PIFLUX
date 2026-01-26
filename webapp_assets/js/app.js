
const { useState, useEffect, useContext, createContext } = React;
const { createRoot } = ReactDOM;
const { MemoryRouter, Routes, Route, Link, useNavigate, useParams, useLocation } = ReactRouterDOM;

// --- i18n Dictionary ---
const TRANSLATIONS = {
    es: {
        nav: { dashboard: "Dashboard", academy: "Academia", formulas: "Fórmulas", games: "Juegos", online: "SISTEMA ONLINE" },
        footer: { legal: "Información Legal", docs: "Documentación Técnica", copyright: "© 2026 PIF Mando Técnico" },
        dashboard: {
            hero_subtitle: "Narrativa Técnica",
            hero_title: "La Aventura del Instalador",
            hero_btn_start: "Comenzar Lectura",
            hero_btn_go: "Ir a la Historia",
            welcome: "Bienvenido de nuevo, Cadete.",
            briefing: "Informe Diario",
            academic_status: "Estado Académico",
            study_goal: "Meta de Estudio",
            terminal_title: "TERMINAL - AntiGravity CLI",
            priority_alert: "Alerta Prioritaria",
            priority_desc: "Entrega del PIF",
            priority_sub: "Fecha Límite Próxima",
            action_req: "Acción Requerida",
            timeline: "Línea de Tiempo Semestral",
            downloads: "Archivo Central de PDFs"
        },
        dojo: {
            title: "ACADEMIA PIF",
            subtitle: "SHONEN DOJO: EDICIÓN LUXEMBURGO v2.0",
            choose_class: "¡Elige tu Clase!",
            enter_class: "ENTRAR A CLASE",
            loading: "Conectando al Backend PIF..."
        },
        formulas: {
            title: "FÓRMULAS Y ANALOGÍAS",
            hydraulic: "PRESIÓN HIDRÁULICA",
            hydraulic_desc: "Imagina una pista de baile llena. ¡Si empujas a todos a una esquina, la presión sube!",
            ohms: "LEY DE OHM",
            ohms_desc: "El voltaje es el empujón. La corriente es la velocidad. ¡La resistencia es qué tan pegajoso es el tobogán!"
        }
    },
    en: {
        nav: { dashboard: "Dashboard", academy: "Training Academy", formulas: "Smart Formulas", games: "Card Games", online: "SYSTEM LIVE" },
        footer: { legal: "Legal Information", docs: "Technical Documentation", copyright: "© 2026 PIF Technical Command" },
        dashboard: {
            hero_subtitle: "Technical Narrative",
            hero_title: "The Installer's Adventure",
            hero_btn_start: "Start Reading",
            hero_btn_go: "Go to Story",
            welcome: "Welcome back, Cadet.",
            briefing: "Daily Briefing",
            academic_status: "Academic Status",
            study_goal: "Study Goal",
            terminal_title: "TERMINAL - AntiGravity CLI",
            priority_alert: "Priority Alert",
            priority_desc: "PIF Submission",
            priority_sub: "Due Date Approaching",
            action_req: "Action Required",
            timeline: "Semester Timeline",
            downloads: "PDF Central Archive"
        },
        dojo: {
            title: "PIF ACADEMY",
            subtitle: "SHONEN DOJO: LUXEMBOURG EDITION v2.0",
            choose_class: "Choose Your Class!",
            enter_class: "ENTER CLASS",
            loading: "Connecting to PIF Backend..."
        },
        formulas: {
            title: "TRADE FORMULAS & ANALOGIES",
            hydraulic: "HYDRAULIC PRESSURE",
            hydraulic_desc: "Imagine a crowded dance floor. If you push everyone into a smaller corner, the stress goes way up!",
            ohms: "OHM'S LAW",
            ohms_desc: "Voltage is the push. Current is the speed. Resistance is how sticky the slide is!"
        }
    },
    fr: {
        nav: { dashboard: "Tableau de Bord", academy: "Académie", formulas: "Formules", games: "Jeux", online: "SYSTÈME EN LIGNE" },
        footer: { legal: "Mentions Légales", docs: "Documentation Technique", copyright: "© 2026 Commandement Technique PIF" },
        dashboard: {
            hero_subtitle: "Narrative Technique",
            hero_title: "L'Aventure de l'Installateur",
            hero_btn_start: "Commencer la Lecture",
            hero_btn_go: "Aller à l'Histoire",
            welcome: "Bon retour, Cadet.",
            briefing: "Briefing Quotidien",
            academic_status: "Statut Académique",
            study_goal: "Objectif d'Étude",
            terminal_title: "TERMINAL - AntiGravity CLI",
            priority_alert: "Alerte Prioritaire",
            priority_desc: "Soumission PIF",
            priority_sub: "Date Limite Approche",
            action_req: "Action Requise",
            timeline: "Chronologie Semestrielle",
            downloads: "Archives Centrales PDF"
        },
        dojo: {
            title: "ACADÉMIE PIF",
            subtitle: "SHONEN DOJO: ÉDITION LUXEMBOURG v2.0",
            choose_class: "Choisis ta Classe !",
            enter_class: "ENTRER EN CLASSE",
            loading: "Connexion au Backend PIF..."
        },
        formulas: {
            title: "FORMULES ET ANALOGIES",
            hydraulic: "PRESSION HYDRAULIQUE",
            hydraulic_desc: "Imaginez une piste de danse bondée. Si vous poussez tout le monde dans un coin, la pression monte !",
            ohms: "LOI D'OHM",
            ohms_desc: "La tension est la poussée. Le courant est la vitesse. La résistance est la rugosité du toboggan !"
        }
    },
    de: {
        nav: { dashboard: "Dashboard", academy: "Akademie", formulas: "Formeln", games: "Spiele", online: "SYSTEM ONLINE" },
        footer: { legal: "Rechtliche Hinweise", docs: "Technische Dokumentation", copyright: "© 2026 PIF Technisches Kommando" },
        dashboard: {
            hero_subtitle: "Technische Erzählung",
            hero_title: "Das Abenteuer des Installateurs",
            hero_btn_start: "Lesen Starten",
            hero_btn_go: "Zur Geschichte",
            welcome: "Willkommen zurück, Kadett.",
            briefing: "Tägliches Briefing",
            academic_status: "Akademischer Status",
            study_goal: "Studienziel",
            terminal_title: "TERMINAL - AntiGravity CLI",
            priority_alert: "Prioritätsalarm",
            priority_desc: "PIF Einreichung",
            priority_sub: "Frist nähert sich",
            action_req: "Handlung Erforderlich",
            timeline: "Semester Zeitplan",
            downloads: "PDF Zentralarchiv"
        },
        dojo: {
            title: "PIF AKADEMIE",
            subtitle: "SHONEN DOJO: LUXEMBURG EDITION v2.0",
            choose_class: "Wähle deine Klasse!",
            enter_class: "KLASSE BETRETEN",
            loading: "Verbindung zum PIF Backend..."
        },
        formulas: {
            title: "HANDELSDATEN & ANALOGIEN",
            hydraulic: "HYDRAULISCHER DRUCK",
            hydraulic_desc: "Stell dir eine volle Tanzfläche vor. Wenn du alle in eine Ecke drückst, steigt der Druck!",
            ohms: "OHMSCHES GESETZ",
            ohms_desc: "Spannung ist der Schub. Strom ist die Geschwindigkeit. Widerstand ist, wie klebrig die Rutsche ist!"
        }
    },
    lb: {
        nav: { dashboard: "Dashboard", academy: "Akademie", formulas: "Formelen", games: "Spiller", online: "SYSTEM ONLINE" },
        footer: { legal: "Legal Informatioun", docs: "Technesch Dokumentatioun", copyright: "© 2026 PIF Technhescht Kommando" },
        dashboard: {
            hero_subtitle: "Technesch Erzielung",
            hero_title: "D'Aventure vum Installateur",
            hero_btn_start: "Lies Starten",
            hero_btn_go: "Op d'Geschicht",
            welcome: "Wëllkomm zréck, Cadet.",
            briefing: "Deegleche Briefing",
            academic_status: "Akademesche Status",
            study_goal: "Studienziel",
            terminal_title: "TERMINAL - AntiGravity CLI",
            priority_alert: "Prioritéit Alarm",
            priority_desc: "PIF Ofginn",
            priority_sub: "Datum kënnt no",
            action_req: "Aktioun Néideg",
            timeline: "Semester Zäitplang",
            downloads: "PDF Zentralarchiv"
        },
        dojo: {
            title: "PIF AKADEMIE",
            subtitle: "SHONEN DOJO: LËTZEBUERG EDITIOUN v2.0",
            choose_class: "Wielt Är Klass!",
            enter_class: "KLASS TRETEN",
            loading: "Verbindung mam PIF Backend..."
        },
        formulas: {
            title: "HANDELSDATEN & ANALOGIEN",
            hydraulic: "HYDRAULESCHEN DROCK",
            hydraulic_desc: "Stellt Iech eng voll Danzpist vir. Wann Dir jiddereen an en Eck dréckt, klëmmt den Drock!",
            ohms: "OHM SENG GESETZ",
            ohms_desc: "Spannung ass de Schub. Stroum ass d'Vitesse. Widderstand ass wéi pecheg d'Rutschbahn ass!"
        }
    },
    pt: {
        nav: { dashboard: "Painel", academy: "Academia", formulas: "Fórmulas", games: "Jogos", online: "SISTEMA ONLINE" },
        footer: { legal: "Informação Legal", docs: "Documentação Técnica", copyright: "© 2026 Comando Técnico PIF" },
        dashboard: {
            hero_subtitle: "Narrativa Técnica",
            hero_title: "A Aventura do Instalador",
            hero_btn_start: "Começar Leitura",
            hero_btn_go: "Ir para História",
            welcome: "Bem-vindo de volta, Cadete.",
            briefing: "Briefing Diário",
            academic_status: "Status Acadêmico",
            study_goal: "Meta de Estudo",
            terminal_title: "TERMINAL - AntiGravity CLI",
            priority_alert: "Alerta Prioritário",
            priority_desc: "Submissão do PIF",
            priority_sub: "Prazo Aproximando",
            action_req: "Ação Necessária",
            timeline: "Linha do Tempo Semestral",
            downloads: "Arquivo Central de PDFs"
        },
        dojo: {
            title: "ACADEMIA PIF",
            subtitle: "SHONEN DOJO: EDIÇÃO LUXEMBURGO v2.0",
            choose_class: "Escolha sua Classe!",
            enter_class: "ENTRAR NA CLASSE",
            loading: "Conectando ao Backend PIF..."
        },
        formulas: {
            title: "FÓRMULAS E ANALOGIAS",
            hydraulic: "PRESSÃO HIDRÁULICA",
            hydraulic_desc: "Imagine uma pista de dança lotada. Se você empurrar todos para um canto, a pressão sobe!",
            ohms: "LEI DE OHM",
            ohms_desc: "Tensão é o empurrão. Corrente é a velocidade. Resistência é o quão pegajoso é o escorregador!"
        }
    }
};

// --- Language Context ---
const LanguageContext = createContext();

const LanguageProvider = ({ children }) => {
    const [language, setLanguage] = useState('es'); // Default Spanish

    const t = (section, key) => {
        try {
            return TRANSLATIONS[language][section][key] || key;
        } catch (e) {
            return key;
        }
    };

    return (
        <LanguageContext.Provider value={{ language, setLanguage, t }}>
            {children}
        </LanguageContext.Provider>
    );
};

const useTranslation = () => useContext(LanguageContext);

// --- API Hooks ---
const useTrades = () => {
    const [trades, setTrades] = useState([]);
    const { language } = useTranslation();

    useEffect(() => {
        // Fetch dynamic JSON based on language
        fetch(`locales/trades_${language}.json?v=2.1`)
            .then(res => {
                if (!res.ok) throw new Error("HTTP " + res.status);
                return res.json();
            })
            .then(data => setTrades(data))
            .catch(e => console.error("Could not load trades list:", e));
    }, [language]); // Reload when language changes

    return trades;
};

const useTradeDetail = (code) => {
    const [data, setData] = useState(null);
    const { language } = useTranslation();
    
    useEffect(() => {
        if (!code) return;
        fetch(`./trades/${code}/${language}.json?v=2.0`)
            .then(res => res.json())
            .then(d => setData(d))
            .catch(e => console.error(e));
    }, [code, language]);
    return data;
};

// --- Components ---

const MetricBar = ({ label, value, trend }) => (
    <div className="p-3 bg-white/5 border border-white/5 rounded-lg">
        <div className="flex justify-between mb-1">
            <span className="text-xs text-slate-400">{label}</span>
            <span className={`text-xs ${trend.includes('+') ? 'text-green-400' : 'text-slate-500'}`}>{trend}</span>
        </div>
        <div className="text-xl font-bold">{value}%</div>
        <div className="w-full bg-white/10 h-1 rounded-full mt-2 overflow-hidden">
            <div className="bg-primary h-full" style={{ width: `${value}%` }}></div>
        </div>
    </div>
);

const MangaClassCard = ({ title, role, color, desc, img, icon, onClick }) => {
    const { t } = useTranslation();
    return (
        <div className="manga-card group overflow-hidden cursor-pointer" onClick={onClick}>
            <div className={`${color} h-64 relative overflow-hidden border-b-[4px] border-[#1a1a1a]`}>
                <div className="halftone absolute inset-0"></div>
                {img ? (
                    <img alt={role} className="absolute inset-0 w-full h-full object-cover mix-blend-multiply opacity-80" src={img} />
                ) : (
                    <div className="absolute inset-0 flex items-center justify-center">
                        <span className="material-symbols-outlined text-[120px] text-black/20">{icon}</span>
                    </div>
                )}
                <div className="absolute bottom-4 right-4 bg-white px-4 py-1 border-2 border-black font-black italic transform -rotate-3 group-hover:rotate-0 transition-transform text-black">
                    {role}
                </div>
            </div>
            <div className="p-6">
                <h3 className="text-3xl font-black mb-2 uppercase italic text-black">{title}</h3>
                <p className="text-sm font-medium mb-6 text-black">{desc}</p>
                <button className="w-full py-3 bg-[#1a1a1a] text-white font-black italic uppercase hover:bg-opacity-80 transition-colors border-2 border-[#1a1a1a]">
                    {t('dojo', 'enter_class')}
                </button>
            </div>
        </div>
    );
};

// --- Layouts ---

const DashboardLayout = ({ children }) => {
    const { t } = useTranslation();
    return (
        <div className="flex h-full grow flex-col dark">
            <header className="flex items-center justify-between border-b border-solid border-white/10 px-6 py-4 glass sticky top-0 z-50">
                <div className="flex items-center gap-4 text-white">
                    <div className="size-6 text-primary">
                        <span className="material-symbols-outlined text-3xl">bolt</span>
                    </div>
                    <h2 className="text-white text-lg font-bold leading-tight tracking-tight">PIF MASTER CONTROL ROOM</h2>
                </div>
                <div className="flex flex-1 justify-end gap-6 items-center">
                    <nav className="hidden md:flex items-center gap-8">
                        <Link className="text-white/60 text-sm font-medium hover:text-white transition-colors" to="/dojo">{t('nav', 'academy')}</Link>
                        <Link className="text-white/60 text-sm font-medium hover:text-white transition-colors" to="/formulas">{t('nav', 'formulas')}</Link>
                        <Link className="text-white/60 text-sm font-medium hover:text-white transition-colors" to="/games">{t('nav', 'games')}</Link>
                    </nav>
                    <div className="flex items-center gap-4">
                        <button className="flex min-w-[120px] items-center justify-center rounded-full h-10 px-4 bg-primary text-white text-sm font-bold shadow-lg shadow-primary/20">
                            <span className="flex items-center gap-2">
                                <span className="size-2 bg-green-400 rounded-full animate-pulse"></span>
                                {t('nav', 'online')}
                            </span>
                        </button>
                    </div>
                </div>
            </header>
            <main className="max-w-[1400px] mx-auto w-full p-6 space-y-6 flex-grow">
                {children}
            </main>
            <footer className="mt-auto py-8 px-10 border-t border-white/5 flex justify-between items-center text-slate-500 text-xs">
                <div className="flex gap-6">
                    <p>{t('footer', 'copyright')}</p>
                    <a className="hover:text-white" href="#">{t('footer', 'legal')}</a>
                    <a className="hover:text-white" href="#">{t('footer', 'docs')}</a>
                </div>
                <div className="flex items-center gap-4">
                    <span className="flex items-center gap-1"><span className="size-1.5 bg-green-500 rounded-full"></span> Firebase Sync OK</span>
                </div>
            </footer>
        </div>
    );
};

const DojoLayout = ({ children }) => {
    const { language, setLanguage, t } = useTranslation();
    
    return (
        <div className="min-h-screen flex bg-[#f0f0f0] text-[#1a1a1a]">
            <aside className="w-24 bg-[#fdfdfd] border-r-[4px] border-[#1a1a1a] flex flex-col items-center py-8 gap-8 sticky top-0 h-screen z-50">
                <Link to="/" className="arcade-btn bg-purple-500 hover:bg-purple-400" title={t('nav', 'dashboard')}>
                    <span className="material-symbols-outlined text-white">dashboard</span>
                </Link>
                <Link to="/dojo" className="arcade-btn bg-red-500 hover:bg-red-400" title="Dojo">
                    <span className="material-symbols-outlined text-white">home</span>
                </Link>
                <Link to="/formulas" className="arcade-btn bg-blue-500 hover:bg-blue-400 cursor-pointer" title="Formulas">
                    <span className="material-symbols-outlined text-white">functions</span>
                </Link>
                <div className="mt-auto flex flex-col gap-2">
                     {['FR', 'EN', 'DE', 'LB', 'ES', 'PT'].map(lang => (
                        <button 
                            key={lang} 
                            onClick={() => setLanguage(lang.toLowerCase())}
                            className={`w-10 h-10 rounded-full font-bold text-xs flex items-center justify-center transition-all ${language === lang.toLowerCase() ? 'bg-[#1a1a1a] text-white scale-110' : 'bg-gray-200 text-gray-600 hover:bg-gray-300'}`}
                        >
                            {lang}
                        </button>
                    ))}
                </div>
            </aside>
            <div className="flex-1 speed-lines bg-[radial-gradient(#1a1a1a_0.5px,transparent_0.5px),linear-gradient(to_right,#e5e5e5_1px,transparent_1px),linear-gradient(to_bottom,#e5e5e5_1px,transparent_1px)] bg-[length:20px_20px,40px_40px,40px_40px]">
                {children}
            </div>
        </div>
    );
};

// --- Screens ---

const FormulasScreen = () => {
    const { t } = useTranslation();
    return (
        <div className="p-8 max-w-7xl mx-auto space-y-8 animate-fade-in-up">
            <h1 className="manga-title font-manga text-6xl uppercase tracking-tighter mb-8">{t('formulas', 'title')}</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="manga-card p-8 bg-blue-50">
                    <h3 className="font-black text-2xl mb-4 flex items-center gap-2"><span className="material-symbols-outlined">water_drop</span> {t('formulas', 'hydraulic')}</h3>
                    <div className="speech-bubble">
                        <p className="text-sm">"{t('formulas', 'hydraulic_desc')}"</p>
                    </div>
                </div>
                <div className="manga-card p-8 bg-yellow-50">
                    <h3 className="font-black text-2xl mb-4 flex items-center gap-2"><span className="material-symbols-outlined">bolt</span> {t('formulas', 'ohms')}</h3>
                    <div className="speech-bubble">
                        <p className="text-sm">"{t('formulas', 'ohms_desc')}"</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

const GamesScreen = () => (
    <div className="p-8 max-w-7xl mx-auto space-y-8 animate-fade-in-up">
        <h1 className="manga-title font-manga text-6xl uppercase tracking-tighter mb-8 bg-red-500 text-white inline-block px-4 rotate-1">CARD BATTLE ARENA</h1>
        <p className="font-marker text-xl">Didactic Training Battles coming soon!</p>
    </div>
);

const ControlRoomScreen = () => {
    const [currentTime, setCurrentTime] = useState(new Date());
    const [selectedYear, setSelectedYear] = useState(1);
    const { t } = useTranslation();
    const navigate = useNavigate();

    useEffect(() => {
        const timer = setInterval(() => setCurrentTime(new Date()), 1000);
        return () => clearInterval(timer);
    }, []);

    return (
        <React.Fragment>
             <div className="flex flex-wrap justify-between items-end gap-3 pb-4">
                <div className="flex flex-col gap-1">
                    <p className="text-white text-4xl font-black tracking-tight">{t('dashboard', 'hero_title')}</p>
                    <p className="text-slate-400 text-lg">{t('dashboard', 'hero_subtitle')}</p>
                </div>
                <div className="flex gap-2 text-sm text-slate-400 bg-white/5 p-2 rounded-lg border border-white/10">
                    <span className="material-symbols-outlined text-sm">schedule</span>
                    <span>System Time: {currentTime.toLocaleTimeString()}</span>
                </div>
            </div>
            
             <div className="grid grid-cols-1 md:grid-cols-4 grid-rows-auto gap-6">
                 {/* Hero Block */}
                <div className="md:col-span-2 md:row-span-2 glass rounded-xl overflow-hidden flex flex-col group relative">
                    <div className="absolute inset-0 bg-gradient-to-t from-background-dark via-transparent to-transparent z-10"></div>
                     <div className="h-[400px] w-full bg-center bg-cover transition-transform duration-700 group-hover:scale-105"
                                style={{ backgroundImage: 'url("images/academy_hub_hero.png")' }}></div>
                     <div className="absolute top-6 left-6 z-20">
                        <span className="bg-primary/90 text-white px-3 py-1 rounded-full text-xs font-bold uppercase tracking-widest">{t('dashboard', 'briefing')}</span>
                    </div>
                    <div className="p-8 relative z-20 flex-1 flex flex-col justify-end gap-4">
                         <div>
                            <h3 className="text-white text-3xl font-bold leading-tight">{t('dashboard', 'welcome')}</h3>
                        </div>
                        <div className="flex items-center justify-between">
                            <button onClick={() => navigate('/dojo')} className="flex min-w-[140px] cursor-pointer items-center justify-center rounded-xl h-12 px-6 bg-primary text-white font-bold hover:scale-105 transition-transform glow-primary">
                                {t('dojo', 'enter_class')}
                            </button>
                        </div>
                    </div>
                </div>

                {/* Stats */}
                 <div className="glass rounded-xl p-6 flex flex-col gap-4">
                    <div className="flex items-center justify-between">
                        <h4 className="text-white font-bold flex items-center gap-2">
                            <span className="material-symbols-outlined text-primary">bar_chart</span>
                            {t('dashboard', 'academic_status')}
                        </h4>
                    </div>
                    <div className="space-y-4">
                        <MetricBar label="Semester" value={65} trend="+1.2%" />
                        <MetricBar label="Assignments" value={88} trend="14/16" />
                    </div>
                </div>
                
                 {/* Terminal */}
                 <div className="glass rounded-xl p-6 bg-black/40 border-primary/20">
                     <div className="cli-text text-sm space-y-2">
                        <p className="text-primary"><span className="text-slate-500">&gt;</span> {t('dashboard', 'terminal_title')}</p>
                        <p className="text-white mt-4 animate-pulse"><span className="text-primary">_</span></p>
                    </div>
                 </div>
                 
                 {/* Priority Alert */}
                 <div className="md:col-span-1 glass rounded-xl overflow-hidden flex flex-col group hover:bg-white/5 transition-colors">
                     <div className="p-6">
                        <h4 className="text-white font-bold flex items-center gap-2 mb-4">
                            <span className="material-symbols-outlined text-primary">notifications_active</span>
                            {t('dashboard', 'priority_alert')}
                        </h4>
                        <p className="text-white font-bold text-lg">{t('dashboard', 'priority_desc')}</p>
                         <div className="mt-4 bg-primary text-white text-xs px-3 py-1 rounded-full font-bold">
                            T-MINUS 48H
                        </div>
                     </div>
                 </div>
             </div>
        </React.Fragment>
    );
};

const DojoScreen = () => {
    const trades = useTrades();
    const navigate = useNavigate();
    const { t } = useTranslation();

    return (
        <div className="p-8 max-w-7xl mx-auto space-y-16">
            <header className="flex justify-between items-center mb-16">
                <div className="flex flex-col">
                    <h1 className="manga-title font-manga text-7xl uppercase tracking-tighter transform -rotate-2">{t('dojo', 'title')}</h1>
                    <p className="font-marker text-xl ml-2 text-[#1a1a1a]">{t('dojo', 'subtitle')}</p>
                </div>
            </header>

            <section>
                <div className="flex items-center gap-4 mb-8">
                    <h2 className="text-4xl font-black italic uppercase">{t('dojo', 'choose_class')}</h2>
                    <div className="h-1 flex-1 bg-[#1a1a1a]"></div>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
                    {trades.length === 0 ? <p className="text-xl italic font-black">{t('dojo', 'loading')}</p> :
                        trades.map(trade => (
                            <MangaClassCard
                                key={trade.code}
                                title={trade.name.split('(')[0]}
                                role={trade.trait.role}
                                color={trade.trait.color}
                                desc={trade.trait.desc}
                                icon={trade.trait.icon}
                                img={trade.trait.img}
                                onClick={() => navigate(`/dojo/${trade.code}`)}
                            />
                        ))}
                </div>
            </section>
        </div>
    );
};

const TradeDetailScreen = () => {
    const { tradeId } = useParams();
    const data = useTradeDetail(tradeId);

    if (!data) return <div className="p-10 font-black text-2xl">LOADING SCROLL DATA...</div>;

    return (
        <div className="p-8 max-w-7xl mx-auto space-y-8 animate-fade-in-up">
            <div className="flex items-center gap-4">
                <Link to="/dojo" className="arcade-btn bg-[#1a1a1a] cursor-pointer hover:bg-red-500">
                    <span className="material-symbols-outlined text-white">arrow_back</span>
                </Link>
                <h1 className="manga-title font-manga text-6xl uppercase tracking-tighter">{data.title}</h1>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div className="space-y-6">
                    {data.sections.map((sec, idx) => (
                        <div key={idx} className="manga-card p-6 hover:bg-[#f0f0f0] cursor-pointer">
                            <h3 className="font-black text-xl italic uppercase mb-2 border-b-2 border-black">{sec.title}</h3>
                            <p className="text-sm font-medium">{sec.content.length} items logged.</p>
                        </div>
                    ))}
                </div>
                <div className="md:col-span-2 manga-card p-8 min-h-[500px] bg-[url('https://www.transparenttextures.com/patterns/graphy.png')]">
                    {data.sections.map((sec, idx) => (
                        <div key={idx} className="mb-12">
                            <h2 className="text-4xl font-black italic uppercase mb-6 bg-yellow-300 inline-block px-2 transform -rotate-1 border-2 border-black shadow-[4px_4px_0_black]">{sec.title}</h2>
                            <div className="space-y-4">
                                {sec.content.map((item, i) => (
                                    <div key={i} className="flex gap-4 items-start group">
                                         <div className="w-8 h-8 bg-black text-white flex items-center justify-center font-black rounded-md group-hover:bg-[#ff007a] transition-colors flex-shrink-0">
                                            {i + 1}
                                        </div>
                                        <div className="speech-bubble flex-1 shadow-md group-hover:shadow-[8px_8px_0_rgba(0,0,0,0.1)] transition-all">
                                            {item.title ? (
                                                <React.Fragment>
                                                    <p className="font-black text-lg uppercase italic">{item.title}</p>
                                                    <p className="text-sm">{item.description || item.url}</p>
                                                </React.Fragment>
                                            ) : (
                                                <React.Fragment>
                                                    <p className="font-bold italic text-red-500 mb-1">Q: {item.question}</p>
                                                    <p className="text-sm border-l-4 border-green-400 pl-2">A: {item.answer}</p>
                                                </React.Fragment>
                                            )}
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

// --- App Root ---

const App = () => {
    return (
        <LanguageProvider>
            <MemoryRouter>
                <Routes>
                    <Route path="/" element={
                        <DashboardLayout>
                            <ControlRoomScreen />
                        </DashboardLayout>
                    } />
                    <Route path="/dojo" element={
                        <DojoLayout>
                            <DojoScreen />
                        </DojoLayout>
                    } />
                    <Route path="/formulas" element={
                        <DojoLayout>
                            <FormulasScreen />
                        </DojoLayout>
                    } />
                     <Route path="/games" element={
                        <DojoLayout>
                            <GamesScreen />
                        </DojoLayout>
                    } />
                    <Route path="/dojo/:tradeId" element={
                        <DojoLayout>
                            <TradeDetailScreen />
                        </DojoLayout>
                    } />
                </Routes>
            </MemoryRouter>
        </LanguageProvider>
    );
};

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);

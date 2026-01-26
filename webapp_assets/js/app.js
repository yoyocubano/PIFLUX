
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
// --- API Hooks ---
const useTrades = () => {
    const [trades, setTrades] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const { language } = useTranslation();

    useEffect(() => {
        setLoading(true);
        setError(null);
        // Fetch dynamic JSON based on language
        fetch(`locales/trades_${language}.json?v=2.2`)
            .then(res => {
                if (!res.ok) throw new Error("HTTP " + res.status);
                return res.json();
            })
            .then(data => {
                setTrades(data);
                setLoading(false);
            })
            .catch(e => {
                console.error("Could not load trades list:", e);
                setError(e);
                setLoading(false);
            });
    }, [language]); 

    return { trades, loading, error };
};

const useTradeDetail = (code) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const { language } = useTranslation();
    
    useEffect(() => {
        if (!code) return;
        setLoading(true);
        fetch(`./trades/${code}/${language}.json?v=2.0`)
            .then(res => {
                if (!res.ok) throw new Error("HTTP " + res.status);
                return res.json();
            })
            .then(d => {
                setData(d);
                setLoading(false);
            })
            .catch(e => {
                console.error(e);
                setError(e);
                setLoading(false);
            });
    }, [code, language]);
    return { data, loading, error };
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
        <div className="manga-card group overflow-hidden cursor-pointer hover:scale-[1.02] transition-transform duration-300" onClick={onClick}>
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
                <h3 className="text-3xl font-black mb-2 uppercase italic text-black leading-none">{title}</h3>
                <p className="text-sm font-medium mb-6 text-black line-clamp-2">{desc}</p>
                <div className="w-full py-3 bg-[#1a1a1a] text-white flex items-center justify-center font-black italic uppercase border-2 border-[#1a1a1a] group-hover:bg-[#ff007a] transition-colors">
                    {t('dojo', 'enter_class')} <span className="material-symbols-outlined ml-2">arrow_forward</span>
                </div>
            </div>
        </div>
    );
};

// --- Layouts ---

const DashboardLayout = ({ children }) => {
    const { t, language, setLanguage } = useTranslation();
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
                     {/* Language Selector (ALWAYS VISIBLE) */}
                    <div className="flex bg-[#1a1a1a] p-1 rounded-lg border border-white/10">
                        {['FR', 'EN', 'DE', 'LB', 'ES', 'PT'].map(lang => (
                             <button 
                                key={lang} 
                                onClick={() => setLanguage(lang.toLowerCase())}
                                className={`px-2 md:px-3 py-1 text-white font-bold text-xs rounded transition-all ${language === lang.toLowerCase() ? 'bg-primary shadow-[0_0_10px_#833cf6]' : 'hover:bg-white/10'}`}
                            >
                                {lang}
                            </button>
                        ))}
                    </div>
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
    const [showPriorityForm, setShowPriorityForm] = useState(false);
    const [showExamCalc, setShowExamCalc] = useState(false);
    const [studyResult, setStudyResult] = useState(null);
    const [examWeeks, setExamWeeks] = useState({});
    const { t } = useTranslation();
    const navigate = useNavigate();

    useEffect(() => {
        const timer = setInterval(() => setCurrentTime(new Date()), 1000);
        return () => clearInterval(timer);
    }, []);

    // Calculation of Academic Context
    const getAcademicStatus = () => {
        const now = new Date();
        const month = now.getMonth(); // 0-11
        let module = "PRE-SESSION";
        let advice = "Prepare for the intake.";

        if (month >= 8 && month <= 10) { module = "MODULE 1"; advice = "Focus: Fundamental Safety & Basic Tools."; } // Sept-Nov
        else if (month === 11 || month <= 1) { module = "MODULE 2"; advice = "Focus: Technical Theory & Circuits."; } // Dec-Feb
        else if (month >= 2 && month <= 4) { module = "MODULE 3"; advice = "Focus: Complex Diagnostics."; } // Mar-May
        else if (month >= 5 && month <= 6) { module = "MODULE 4"; advice = "Focus: PIF Submission & Final Jury."; } // Jun-Jul
        else { module = "SUMMER OPS"; advice = "Review materials. Rest & Recover."; }

        return { module, advice };
    };

    const status = getAcademicStatus();
    const yearAdvice = {
        1: "Year 1 Objective: Master the basics. Safety first. Build your toolkit.",
        2: "Year 2 Objective: Deep technical mastery. Solve complex faults.",
        3: "Year 3 Objective: JURY READY. Perfect your PIF. Lead the team."
    };

    return (
        <React.Fragment>
            {/* Exam Calculator Modal */}
            {showExamCalc && (
                <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center backdrop-blur-sm animate-fade-in-up">
                    <div className="bg-[#1a1a1a] border-2 border-primary p-8 rounded-xl w-full max-w-md shadow-[0_0_50px_rgba(124,58,237,0.3)]">
                        <h3 className="text-primary text-2xl font-black uppercase mb-2 flex items-center gap-2">
                            <span className="material-symbols-outlined">timer</span> Exam Strategy Calculator
                        </h3>
                        <p className="text-slate-400 text-sm mb-6">Input your target date. We will calculate the required grind.</p>

                        <div className="space-y-4">
                            <div>
                                <label className="text-white text-xs font-bold uppercase ml-1">Next Exam Date</label>
                                <input
                                    type="date"
                                    className="w-full bg-white/10 border border-white/20 rounded p-3 text-white focus:outline-none focus:border-primary text-lg"
                                    onChange={(e) => {
                                        const date = new Date(e.target.value);
                                        const now = new Date();
                                        const diffTime = date - now;
                                        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
                                        let hours = 0;
                                        let intensity = "";

                                        if (diffDays <= 3) { hours = 10; intensity = "MAXIMUM OVERDRIVE"; }
                                        else if (diffDays <= 7) { hours = 6; intensity = "HIGH INTENSITY"; }
                                        else if (diffDays <= 30) { hours = 3; intensity = "CONSISTENT GRIND"; }
                                        else { hours = 1; intensity = "MAINTENANCE MODE"; }

                                        setStudyResult({ days: diffDays, hours, intensity });
                                    }}
                                />
                            </div>

                            {studyResult && (
                                <div className="bg-white/5 rounded-xl p-4 border border-white/10 mt-4 animate-pulse">
                                    <div className="flex justify-between items-center mb-2">
                                        <span className="text-slate-400 text-xs uppercase font-bold">Time Remaining</span>
                                        <span className="text-white font-mono">{studyResult.days} DAYS</span>
                                    </div>
                                    <div className="flex justify-between items-center mb-2">
                                        <span className="text-slate-400 text-xs uppercase font-bold">Required Study</span>
                                        <span className="text-[#00ff2f] font-black text-xl">{studyResult.hours} HOURS / DAY</span>
                                    </div>
                                    <div className="mt-2 text-center">
                                        <span className="bg-primary text-white text-xs font-black px-2 py-1 rounded">{studyResult.intensity}</span>
                                    </div>
                                </div>
                            )}

                            <div className="flex justify-end gap-2 mt-6">
                                <button type="button" onClick={() => setShowExamCalc(false)} className="px-4 py-2 text-slate-400 hover:text-white font-bold text-sm">CLOSE</button>
                            </div>
                        </div>
                    </div>
                </div>
            )}

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
                             <p className="text-primary text-sm font-bold tracking-widest uppercase mb-2">Semester 1 • {status.module}</p>
                            <h3 className="text-white text-3xl font-bold leading-tight">{t('dashboard', 'welcome')}</h3>
                        </div>
                         <div className="flex h-12 items-center justify-center rounded-xl bg-white/5 p-1 border border-white/10 w-full max-w-md">
                            {[1, 2, 3].map(num => (
                                <label key={num} onClick={() => setSelectedYear(num)} className={`flex cursor-pointer h-full grow items-center justify-center rounded-lg px-2 text-sm font-bold transition-all ${selectedYear === num ? 'bg-primary text-white' : 'text-slate-400 hover:text-white'}`}>
                                    <span>{num}{num === 1 ? 'st' : num === 2 ? 'nd' : 'rd'} Year</span>
                                </label>
                            ))}
                        </div>
                        <div className="flex items-center justify-between">
                             <p className="text-slate-300 max-w-xs italic text-sm">"{yearAdvice[selectedYear]}"</p>
                            <button onClick={() => navigate('/dojo')} className="flex min-w-[140px] cursor-pointer items-center justify-center rounded-xl h-12 px-6 bg-primary text-white font-bold hover:scale-105 transition-transform glow-primary">
                                {t('dojo', 'enter_class')}
                            </button>
                        </div>
                    </div>
                </div>

                {/* Stats Clickable -> Opens Calculator */}
                 <div onClick={() => setShowExamCalc(true)} className="glass rounded-xl p-6 flex flex-col gap-4 cursor-pointer hover:bg-white/5 transition-colors group relative">
                    <div className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity">
                         <span className="material-symbols-outlined text-sm text-primary">edit</span>
                    </div>
                    <div className="flex items-center justify-between">
                        <h4 className="text-white font-bold flex items-center gap-2">
                            <span className="material-symbols-outlined text-primary">bar_chart</span>
                            {t('dashboard', 'academic_status')}
                        </h4>
                         <span className="text-[10px] text-green-400 font-mono">ONLINE</span>
                    </div>
                    <div className="space-y-4 pointer-events-none">
                        <MetricBar label="Semester" value={65} trend="+1.2%" />
                        <MetricBar label="Assignments" value={88} trend="14/16" />
                    </div>
                     {studyResult && (
                        <div className="mt-2 pt-2 border-t border-white/10">
                            <p className="text-xs text-slate-400 uppercase font-bold">Study Goal</p>
                            <p className="text-lg font-black text-[#00ff2f]">{studyResult.hours}H / DAY</p>
                        </div>
                    )}
                </div>
                
                 {/* Terminal */}
                 <div className="glass rounded-xl p-6 bg-black/40 border-primary/20">
                     <div className="cli-text text-sm space-y-2">
                        <p className="text-primary"><span className="text-slate-500">&gt;</span> {t('dashboard', 'terminal_title')}</p>
                         <p className="text-primary"><span className="text-slate-500">&gt;</span> Current Module: <span className="text-blue-400">{status.module}</span></p>
                        <p className="text-primary"><span className="text-slate-500">&gt;</span> System Msg: <span className="text-slate-400 italic">"{status.advice}"</span></p>
                         {studyResult ? (
                            <div className="mt-2 text-xs border-l-2 border-green-500 pl-2">
                                <p className="text-white">TARGET: <span className="text-green-400 font-bold">{studyResult.days} DAYS LEFT</span></p>
                                <p className="text-white">REQUIRED: <span className="text-[#00ff2f] font-black">{studyResult.hours}H / DAY</span></p>
                            </div>
                        ) : (
                            <p className="text-primary"><span className="text-slate-500">&gt;</span> Status: <span className="text-slate-400">WAITING FOR INPUT...</span></p>
                        )}
                        <p className="text-white mt-4 animate-pulse"><span className="text-primary">_</span></p>
                    </div>
                 </div>
                 
                 {/* Priority Alert */}
                 <div id="priority-alert-card" className="md:col-span-1 glass rounded-xl overflow-hidden flex flex-col group hover:bg-white/5 transition-colors">
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

                 {/* Timeline with Click Events */}
                <div className="md:col-span-3 glass rounded-xl p-8 flex flex-col gap-8 relative overflow-hidden">
                    <div className="flex items-center justify-between z-10">
                        <div>
                            <h4 className="text-white font-bold text-xl flex items-center gap-2">
                                <span className="material-symbols-outlined text-primary">timeline</span>
                                {t('dashboard', 'timeline')}
                            </h4>
                            <p className="text-slate-400 text-sm">Track your progress. <span className="text-[#00ff2f]">Click points to set Exam Dates.</span></p>
                        </div>
                    </div>

                    <div className="custom-scrollbar flex-1 overflow-x-auto overflow-y-visible pb-4 px-4" ref={(el) => { if (el) el.scrollLeft = el.scrollWidth / 2 - el.clientWidth / 2; }}>
                        <div className="relative h-32 flex items-center min-w-max mx-auto px-12">
                            <div className="absolute inset-x-0 top-1/2 -translate-y-1/2 h-1 bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
                            <div className="flex justify-between gap-12 relative z-10">
                                {Array.from({ length: 16 }).map((_, i) => {
                                    const weekOffset = i - 6;
                                    const now = new Date();
                                    const startOfYear = new Date(now.getFullYear(), 8, 1);
                                    if (now < startOfYear) startOfYear.setFullYear(now.getFullYear() - 1);
                                    const currentWeekNum = Math.ceil((now - startOfYear) / (1000 * 60 * 60 * 24 * 7));
                                    const displayWeek = currentWeekNum + weekOffset;
                                    const displayWeekString = `WK ${displayWeek}`;
                                    const isCurrent = weekOffset === 0;
                                    const isExam = examWeeks[displayWeekString];

                                    return (
                                        <div
                                            key={i}
                                            onClick={() => {
                                                setExamWeeks(prev => ({ ...prev, [displayWeekString]: !prev[displayWeekString] }));
                                                if(!isExam) setShowExamCalc(true); // Open calculator when marking an exam
                                            }}
                                            className="group relative flex flex-col items-center justify-center cursor-pointer"
                                        >
                                            <div className={`
                                                size-4 rounded-full border-2 transition-all duration-300 relative z-20
                                                ${isExam ? 'bg-red-500 border-red-500 shadow-[0_0_15px_red] scale-125'
                                                    : isCurrent ? 'bg-[#1a1a1a] border-[#00ff2f] shadow-[0_0_15px_#00ff2f] scale-125'
                                                        : 'bg-[#1a1a1a] border-slate-600 group-hover:border-white group-hover:scale-110'}
                                            `}>
                                                {isCurrent && <div className="absolute inset-0 bg-[#00ff2f] rounded-full animate-ping opacity-75"></div>}
                                            </div>
                                            {isCurrent && (
                                                <div className="absolute top-8 flex flex-col items-center animate-bounce z-30">
                                                    <div className="w-0 h-0 border-l-[8px] border-l-transparent border-r-[8px] border-r-transparent border-b-[10px] border-b-[#00ff2f] drop-shadow-[0_0_10px_rgba(0,255,47,0.8)]"></div>
                                                    <span className="text-[#00ff2f] text-[10px] font-black tracking-widest uppercase mt-1">YOU</span>
                                                </div>
                                            )}
                                            <div className={`absolute -top-8 text-[10px] font-bold tracking-widest whitespace-nowrap transition-colors ${isCurrent ? 'text-[#00ff2f]' : isExam ? 'text-red-500' : 'text-slate-500'}`}>
                                                {displayWeekString}
                                            </div>
                                            {isExam && (
                                                <div className="absolute -bottom-8 text-red-500 text-[9px] font-black uppercase tracking-wider bg-red-500/10 px-2 py-0.5 rounded border border-red-500/20">EXAM</div>
                                            )}
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                </div>
             </div>
        </React.Fragment>
    );
};

const DojoScreen = () => {
    const { trades, loading, error } = useTrades();
    const navigate = useNavigate();
    const { t } = useTranslation();

    return (
        <div className="p-8 max-w-7xl mx-auto space-y-16">
            <header className="flex justify-between items-center mb-16">
                <div className="flex flex-col">
                    <h1 className="manga-title font-manga text-7xl uppercase tracking-tighter transform -rotate-2">{t('dojo', 'title')}</h1>
                    <p className="font-marker text-xl ml-2 text-[#1a1a1a]">{t('dojo', 'subtitle')}</p>
                </div>
                {/* Language Selector */}
                <div className="flex bg-[#1a1a1a] p-1 rounded-lg border-2 border-[#1a1a1a] shadow-[4px_4px_0_rgba(0,0,0,0.2)]">
                    {/* ... kept for future ref ... */}
                </div>
            </header>

            <section>
                <div className="flex items-center gap-4 mb-8">
                    <h2 className="text-4xl font-black italic uppercase">{t('dojo', 'choose_class')}</h2>
                    <div className="h-1 flex-1 bg-[#1a1a1a]"></div>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
                    {loading ? (
                         <div className="col-span-3 flex justify-center py-20">
                            <div className="text-3xl font-black italic animate-bounce">{t('dojo', 'loading')}</div>
                         </div>
                    ) : error ? (
                        <div className="col-span-3 bg-red-100 border-l-4 border-red-500 text-red-700 p-4" role="alert">
                            <p className="font-bold">Error loading classes</p>
                            <p>{error.message}</p>
                        </div>
                    ) : (
                        trades.map(trade => (
                            <MangaClassCard
                                key={trade.code}
                                title={trade.name.split('(')[0]}
                                role={trade.trait.role}
                                color={trade.trait.color}
                                desc={trade.trait.desc}
                                icon={trade.trait.icon}
                                img={trade.trait.img}
                                backContent={trade.back_content}
                                onClick={() => navigate(`/dojo/${trade.code}`)}
                            />
                        ))
                    )}
                </div>
            </section>
        </div>
    );
};

const TradeDetailScreen = () => {
    const { tradeId } = useParams();
    const { data, loading, error } = useTradeDetail(tradeId);
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [selectedItem, setSelectedItem] = useState(null);

    // Auto-select first category on load
    useEffect(() => {
        if (data && data.sections && data.sections.length > 0 && !selectedCategory) {
            setSelectedCategory(data.sections[0]);
        }
    }, [data]);

    if (loading) return <div className="p-10 font-black text-2xl animate-pulse">LOADING SCROLL DATA...</div>;
    if (error) return <div className="p-10 font-black text-2xl text-red-600">ERROR LOADING DATA: {error.message}</div>;
    if (!data) return null;

    return (
        <React.Fragment>
            {/* ITEM DETAIL MODAL (HTML VIEWER) */}
            {selectedItem && (
                <div className="fixed inset-0 bg-black/90 z-[100] flex items-center justify-center p-4 backdrop-blur-md animate-fade-in-up" onClick={() => setSelectedItem(null)}>
                    <div className="bg-white border-[4px] border-[#1a1a1a] w-full max-w-2xl shadow-[0_0_50px_rgba(255,255,255,0.2)] relative flex flex-col max-h-[90vh]" onClick={e => e.stopPropagation()}>
                        
                        {/* Modal Header */}
                        <div className="bg-[#1a1a1a] text-white p-4 flex justify-between items-center border-b-4 border-black">
                            <h3 className="font-manga text-3xl uppercase tracking-wider text-yellow-400">
                                {selectedItem.title ? 'OPERATIONAL DATA' : 'EXAM QUERY'}
                            </h3>
                            <button 
                                onClick={() => setSelectedItem(null)}
                                className="text-white hover:text-red-500 transition-colors"
                            >
                                <span className="material-symbols-outlined text-3xl">close</span>
                            </button>
                        </div>

                        {/* Modal Content */}
                        <div className="p-8 overflow-y-auto bg-[url('https://www.transparenttextures.com/patterns/graphy.png')]">
                            {selectedItem.title ? (
                                <React.Fragment>
                                    <h2 className="text-3xl font-black italic uppercase mb-6 leading-none border-b-2 border-black pb-4">
                                        {selectedItem.title}
                                    </h2>
                                    <div className="prose prose-lg max-w-none font-medium text-slate-800">
                                        {/* SECURITY: Content from local JSON. For untrusted input, Use Sanitizer. */}
                                        <p dangerouslySetInnerHTML={{ __html: selectedItem.description || selectedItem.url }} />
                                        
                                        {/* Mock "Extended HTML Content" if description is short */}
                                        <div className="mt-8 p-4 bg-yellow-50 border-l-4 border-yellow-400 text-sm font-mono text-yellow-800">
                                            <strong>System Note:</strong> Full technical documentation for this protocol is currently compiled in the secure archive.
                                        </div>
                                    </div>
                                </React.Fragment>
                            ) : (
                                <div className="space-y-6">
                                    <div className="bg-red-50 p-6 border-l-8 border-red-500 rounded-r-lg">
                                        <p className="text-xs font-black uppercase text-red-400 mb-2">THE QUESTION</p>
                                        <p className="font-black text-2xl italic text-[#1a1a1a]">"{selectedItem.question}"</p>
                                    </div>
                                    
                                    <div className="flex justify-center">
                                        <span className="material-symbols-outlined text-4xl text-slate-300">arrow_downward</span>
                                    </div>

                                    <div className="bg-green-50 p-6 border-l-8 border-green-500 rounded-r-lg shadow-lg">
                                         <p className="text-xs font-black uppercase text-green-600 mb-2">THE ANSWER</p>
                                        <p className="text-xl font-bold text-green-900">{selectedItem.answer}</p>
                                    </div>
                                </div>
                            )}
                        </div>

                        {/* Modal Footer */}
                        <div className="p-4 bg-gray-100 border-t-2 border-black flex justify-end">
                            <button 
                                onClick={() => setSelectedItem(null)}
                                className="px-6 py-2 bg-[#1a1a1a] text-white font-black italic uppercase hover:bg-[#ff007a] transition-colors border-2 border-black shadow-[4px_4px_0_black] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0_black]"
                            >
                                CLOSE TERMINAL
                            </button>
                        </div>
                    </div>
                </div>
            )}

            <div className="p-4 md:p-8 max-w-[1600px] mx-auto space-y-6 h-[calc(100vh-80px)] flex flex-col animate-fade-in-up">
                
                {/* Header */}
                <div className="flex items-center gap-4 flex-shrink-0">
                    <Link to="/dojo" className="bg-[#1a1a1a] w-12 h-12 flex items-center justify-center border-2 border-white hover:bg-red-600 transition-colors shadow-[4px_4px_0_rgba(255,255,255,0.3)]">
                        <span className="material-symbols-outlined text-white">arrow_back</span>
                    </Link>
                    <div>
                         <h1 className="manga-title font-manga text-4xl md:text-6xl uppercase tracking-tighter leading-none">{data.title}</h1>
                         <div className="flex items-center gap-2 text-[#ff007a] font-mono text-xs uppercase font-bold">
                            <span className="w-2 h-2 bg-[#ff007a] inline-block animate-pulse"></span>
                            Secure Connection Established
                         </div>
                    </div>
                </div>

                {/* Main Split Layout */}
                <div className="flex flex-col md:flex-row gap-8 grow overflow-hidden">
                    
                    {/* LEFT COL: CATEGORIES */}
                    <div className="w-full md:w-1/3 lg:w-1/4 flex flex-col gap-4 overflow-y-auto pr-2 pb-10">
                         <div className="bg-yellow-100 p-3 border-2 border-black text-xs font-bold uppercase tracking-wide mb-2 sticky top-0 z-10 shadow-sm">
                            Directory
                        </div>
                        {data.sections.map((sec, idx) => (
                            <button 
                                key={idx} 
                                onClick={() => setSelectedCategory(sec)}
                                className={`p-6 text-left border-[3px] transition-all relative group
                                    ${selectedCategory === sec 
                                        ? 'bg-[#1a1a1a] text-white border-white shadow-[8px_8px_0_rgba(255,255,255,0.3)] translate-x-2' 
                                        : 'bg-white text-black border-black hover:bg-yellow-300 hover:shadow-[8px_8px_0_black]'}
                                `}
                            >
                                <h3 className="font-black text-2xl italic uppercase leading-none mb-1">{sec.title}</h3>
                                <div className="flex justify-between items-end">
                                    <span className="text-xs font-mono opacity-80">{sec.content.length} FILES</span>
                                    {selectedCategory === sec && <span className="material-symbols-outlined animate-bounce">arrow_right_alt</span>}
                                </div>
                            </button>
                        ))}
                    </div>

                    {/* RIGHT COL: ITEMS BOARD */}
                    <div className="flex-1 bg-[#f0f0f0] border-[4px] border-[#1a1a1a] p-6 md:p-8 relative shadow-[inset_0_0_20px_rgba(0,0,0,0.1)] overflow-hidden flex flex-col">
                        <div className="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/graphy.png')] pointer-events-none"></div>
                        
                        {/* Header for Right Board */}
                         <div className="flex justify-between items-end mb-8 border-b-4 border-black pb-4 bg-white/50 p-4 backdrop-blur-sm z-10">
                            <h2 className="text-4xl font-black italic uppercase bg-yellow-400 inline-block px-3 py-1 transform -rotate-1 border-2 border-black shadow-[4px_4px_0_black]">
                                {selectedCategory ? selectedCategory.title : 'SELECT DIRECTORY'}
                            </h2>
                            <div className="text-right hidden md:block">
                                <p className="font-mono text-xs text-slate-500">ACCESS LEVEL: UNLIMITED</p>
                                <p className="font-mono text-xs text-slate-500">DECRYPTION: ENABLED</p>
                            </div>
                         </div>

                        {/* Items Grid */}
                        <div className="overflow-y-auto pr-4 pb-20 custom-scrollbar grid grid-cols-1 gap-4 content-start">
                            {selectedCategory ? (
                                selectedCategory.content.map((item, i) => (
                                    <div 
                                        key={i} 
                                        onClick={() => setSelectedItem(item)}
                                        className="bg-white p-6 border-[3px] border-black shadow-[6px_6px_0_rgba(0,0,0,0.15)] hover:shadow-[10px_10px_0_rgba(255,0,122,1)] hover:-translate-y-1 hover:-translate-x-1 transition-all cursor-pointer group flex items-start gap-4"
                                    >
                                        <div className="w-10 h-10 bg-[#1a1a1a] text-white flex items-center justify-center font-black text-lg rounded group-hover:bg-[#ff007a] transition-colors flex-shrink-0">
                                            {i + 1}
                                        </div>
                                        <div className="flex-1">
                                            {item.title ? (
                                                <h4 className="font-black text-xl uppercase italic text-[#1a1a1a] group-hover:text-[#ff007a] transition-colors mb-1">{item.title}</h4>
                                            ) : (
                                                 <h4 className="font-black text-lg italic text-[#1a1a1a] group-hover:text-red-600 transition-colors mb-1">"{item.question}"</h4>
                                            )}
                                            
                                            <p className="text-xs font-bold text-slate-400 uppercase tracking-widest group-hover:text-black">
                                                CLICK TO OPEN FILE
                                            </p>
                                        </div>
                                        <span className="material-symbols-outlined text-slate-300 group-hover:text-black">folder_open</span>
                                    </div>
                                ))
                            ) : (
                                <div className="h-full flex items-center justify-center flex-col opacity-50">
                                    <span className="material-symbols-outlined text-8xl mb-4">move_to_inbox</span>
                                    <p className="font-black text-xl">WAITING FOR INPUT...</p>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    );
};

// --- App Root ---


// --- Error Boundary ---
class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true, error };
    }

    componentDidCatch(error, errorInfo) {
        console.error("Uncaught error:", error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            return (
                <div className="flex h-screen w-full items-center justify-center bg-black text-red-500 font-mono flex-col p-8 text-center">
                    <span className="material-symbols-outlined text-6xl mb-4 animate-pulse">warning</span>
                    <h1 className="text-4xl font-black mb-4">CRITICAL SYSTEM FAILURE</h1>
                    <p className="text-xl mb-8">The PIF control system has encountered an anomaly.</p>
                    <div className="bg-red-900/20 p-4 rounded border border-red-500/50 max-w-2xl overflow-auto text-left">
                        <p className="font-bold">Error Trace:</p>
                        <pre className="text-sm mt-2">{this.state.error && this.state.error.toString()}</pre>
                    </div>
                    <button 
                        onClick={() => window.location.reload()} 
                        className="mt-8 px-6 py-3 bg-red-600 text-white font-bold rounded hover:bg-red-500 transition-colors uppercase"
                    >
                        Reboot System
                    </button>
                    <p className="mt-8 text-slate-500 text-xs">Error Code: ANOMALY_DETECTED_0x99</p>
                </div>
            );
        }

        return this.props.children;
    }
}

// --- App Root ---

const App = () => {
    return (
        <ErrorBoundary>
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
        </ErrorBoundary>
    );
};


const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);

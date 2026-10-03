<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yojana Setu - React Clone</title>
    
    <!-- 1. Load React, ReactDOM, and Babel from the Cloud -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    
    <!-- 2. Load Tailwind CSS from the Cloud -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-slate-200 antialiased selection:bg-cyan-900 selection:text-cyan-50">
    <!-- This is where React will inject our app -->
    <div id="root"></div>

    <!-- 3. Write our React App (type="text/babel" translates this in the browser) -->
    <script type="text/babel">
        const { useState } = React;

        // The Scheme Database
        const schemesDB = [
            {
                id: 1, 
                title: "Post-Matric Scholarship for SC Students", 
                occupation: "student",
                pillar: "LIBERTY",
                status: "Possibly Eligible",
                score: "73",
                description: "Financial assistance to Scheduled Caste students studying at post-matriculation or post-secondary stage.",
                benefit: "100% compulsory non-refundable college fees reimbursement plus monthly maintenance allowance directly credited via DBT."
            },
            {
                id: 2, 
                title: "Atal Pension Yojana (APY)", 
                occupation: "all",
                pillar: "FRATERNITY",
                status: "Possibly Eligible",
                score: "60",
                description: "Government-backed guaranteed pension scheme for unorganised sector workers between 18 and 40 years.",
                benefit: "Guaranteed minimum monthly pension of ₹1,000, ₹2,000, ₹3,000, ₹4,000 or ₹5,000 from age 60 until lifetime."
            }
        ];

        function App() {
            // React State for the dropdown
            const [occupation, setOccupation] = useState("all");

            // Filter logic
            const filteredSchemes = schemesDB.filter(
                scheme => scheme.occupation === occupation || scheme.occupation === "all"
            );

            return (
                <div class="min-h-screen flex flex-col md:flex-row max-w-7xl mx-auto">
                    
                    {/* Left Sidebar: The Questionnaire */}
                    <div class="w-full md:w-1/3 p-8 border-r border-slate-800">
                        <div class="inline-block bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold px-3 py-1 rounded-full mb-6">
                            🔒 Your answers stay on this device
                        </div>
                        <h1 class="text-4xl font-extrabold text-white mb-2">Yojana Setu</h1>
                        <p class="text-slate-400 text-sm mb-8">Government Scheme Finder & Application Guide.<br/>Discover what you qualify for in under 2 minutes.</p>
                        
                        <div class="mb-6">
                            <label class="block text-slate-300 text-sm font-bold mb-2">Your Occupation:</label>
                            <select 
                                class="w-full bg-slate-800 border border-slate-700 text-white rounded-lg p-3 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500"
                                value={occupation}
                                onChange={(e) => setOccupation(e.target.value)}
                            >
                                <option value="all">Show All</option>
                                <option value="student">Student</option>
                                <option value="business">Business</option>
                                <option value="farmer">Farmer</option>
                            </select>
                        </div>
                        
                        <div class="bg-slate-800/50 rounded-lg p-4 border border-slate-700/50">
                            <p class="text-xs text-slate-400">💡 Answer more questions to unlock targeted schemes.</p>
                        </div>
                    </div>

                    {/* Right Side: The Results Dashboard */}
                    <div class="w-full md:w-2/3 p-8 bg-[#0b1120]">
                        <div class="flex justify-between items-end mb-6">
                            <h2 class="text-xl font-bold text-white">{filteredSchemes.length} Schemes Found</h2>
                        </div>

                        {/* Render the Scheme Cards */}
                        {filteredSchemes.map(scheme => (
                            <div key={scheme.id} class="bg-slate-800 border border-slate-700 rounded-xl p-6 mb-6 hover:border-slate-500 transition-colors duration-200 relative overflow-hidden">
                                
                                {/* Orange Accent Line */}
                                <div class="absolute left-0 top-0 bottom-0 w-1 bg-orange-500"></div>

                                <div class="flex gap-3 mb-4">
                                    <span class="bg-emerald-500/10 text-emerald-400 px-3 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider">
                                        {scheme.status}
                                    </span>
                                    <span class="bg-sky-500/10 text-sky-400 px-3 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider">
                                        {scheme.pillar}
                                    </span>
                                </div>
                                
                                <h3 class="text-xl font-bold text-white mb-2">{scheme.title}</h3>
                                <p class="text-sm text-slate-400 mb-4">{scheme.description}</p>
                                
                                <div class="border-l-2 border-blue-500 pl-3 mb-6">
                                    <p class="text-sm text-slate-300"><span class="font-bold text-white">Benefit:</span> {scheme.benefit}</p>
                                </div>

                                <div class="flex justify-between items-center pt-4 border-t border-slate-700/50 mt-4">
                                    <div class="text-xs text-slate-400 font-medium">
                                        Relevance: <span class="text-white text-base font-bold">{scheme.score}</span>/100
                                    </div>
                                    <button class="text-sky-400 text-sm font-bold hover:text-sky-300">
                                        Details &rarr;
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            );
        }

        // 4. Render the App to the screen
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>

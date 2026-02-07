import { Github, Twitter, Linkedin } from 'lucide-react';

export const Footer = () => {
    return (
        <footer className="border-t border-white/5 bg-black/40 backdrop-blur-sm mt-auto z-10 relative">
            <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
                <div className="flex flex-col md:flex-row justify-between items-center">
                    <div className="mb-4 md:mb-0">
                        <span className="text-lg font-bold font-mono text-text-primary">
                            QUANTUM<span className="text-accent-1">NEXUS</span>
                        </span>
                        <p className="text-xs text-text-secondary mt-1 font-mono">
                            Advanced Research Interface v1.0.4
                        </p>
                    </div>

                    <div className="flex space-x-6">
                        <a href="#" className="text-text-secondary hover:text-accent-1 transition-colors">
                            <Github className="h-5 w-5" />
                        </a>
                        <a href="#" className="text-text-secondary hover:text-accent-1 transition-colors">
                            <Twitter className="h-5 w-5" />
                        </a>
                        <a href="#" className="text-text-secondary hover:text-accent-1 transition-colors">
                            <Linkedin className="h-5 w-5" />
                        </a>
                    </div>
                </div>
                <div className="mt-8 text-center text-xs text-text-secondary font-mono">
                    &copy; {new Date().getFullYear()} Quantum Nexus. All systems nominal.
                </div>
            </div>
        </footer>
    );
};

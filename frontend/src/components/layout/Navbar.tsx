import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/Button';
import { Menu, X, Atom } from 'lucide-react';

export const Navbar = () => {
    const [isOpen, setIsOpen] = React.useState(false);
    const location = useLocation();

    const links = [
        { name: 'Home', path: '/' },
        { name: 'Assistant', path: '/assistant' },
        { name: 'About', path: '/about' },
        { name: 'Contact', path: '/contact' },
    ];

    return (
        <nav className="fixed top-0 left-0 right-0 z-50 glass border-b border-white/5">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <Link to="/" className="flex items-center space-x-2 group">
                            <div className="relative w-8 h-8 flex items-center justify-center bg-accent-1/10 rounded-full group-hover:bg-accent-1/20 transition-colors">
                                <Atom className="w-5 h-5 text-accent-1 animate-pulse-slow" />
                                <div className="absolute inset-0 rounded-full ring-1 ring-accent-1/30 animate-pulse-slow" />
                            </div>
                            <span className="text-xl font-bold font-mono tracking-tighter text-text-primary group-hover:text-white transition-colors">
                                QUANTUM<span className="text-accent-1">NEXUS</span>
                            </span>
                        </Link>
                    </div>

                    <div className="hidden md:block">
                        <div className="ml-10 flex items-baseline space-x-8">
                            {links.map((link) => (
                                <Link
                                    key={link.name}
                                    to={link.path}
                                    className={cn(
                                        "text-sm font-medium transition-colors hover:text-accent-1 relative group font-mono",
                                        location.pathname === link.path ? "text-accent-1" : "text-text-secondary"
                                    )}
                                >
                                    {link.name}
                                    <span className={cn(
                                        "absolute -bottom-1 left-0 w-0 h-0.5 bg-accent-1 transition-all group-hover:w-full",
                                        location.pathname === link.path && "w-full"
                                    )} />
                                </Link>
                            ))}
                        </div>
                    </div>

                    <div className="hidden md:block">
                        <Button variant="outline" size="sm" className="ml-4">
                            Launch Terminal
                        </Button>
                    </div>

                    <div className="md:hidden">
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className="text-text-secondary hover:text-white focus:outline-none"
                        >
                            {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile menu */}
            {isOpen && (
                <div className="md:hidden glass border-b border-white/5 absolute w-full">
                    <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                        {links.map((link) => (
                            <Link
                                key={link.name}
                                to={link.path}
                                onClick={() => setIsOpen(false)}
                                className={cn(
                                    "block px-3 py-2 rounded-md text-base font-medium hover:text-accent-1 hover:bg-white/5 transition-colors font-mono",
                                    location.pathname === link.path ? "text-accent-1 bg-white/5" : "text-text-secondary"
                                )}
                            >
                                {link.name}
                            </Link>
                        ))}
                        <div className="pt-4 pb-2">
                            <Button variant="outline" className="w-full">Launch Terminal</Button>
                        </div>
                    </div>
                </div>
            )}
        </nav>
    );
};

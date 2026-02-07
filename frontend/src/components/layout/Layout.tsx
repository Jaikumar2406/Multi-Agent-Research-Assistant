import React from 'react';
import { Navbar } from './Navbar';
import { Footer } from './Footer';

interface LayoutProps {
    children: React.ReactNode;
}

export const Layout = ({ children }: LayoutProps) => {
    return (
        <div className="min-h-screen flex flex-col bg-background text-text-primary font-sans selection:bg-accent-1/30 selection:text-white">
            {/* Background patterns/effects could go here */}
            <div className="fixed inset-0 z-0 pointer-events-none bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-accent-2/10 via-background to-background opacity-50" />
            <div className="fixed inset-0 z-0 pointer-events-none opacity-20 bg-subtle-grid" />

            <Navbar />

            <main className="flex-grow pt-16 z-10 relative">
                {children}
            </main>

            <Footer />
        </div>
    );
};

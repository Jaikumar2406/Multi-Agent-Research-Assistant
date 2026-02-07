import React from 'react';
import { cn } from '@/lib/utils';
import { Loader2 } from 'lucide-react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'neon';
    size?: 'sm' | 'md' | 'lg' | 'icon';
    isLoading?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
    ({ className, variant = 'primary', size = 'md', isLoading, children, ...props }, ref) => {
        const baseStyles = "inline-flex items-center justify-center rounded-md font-medium transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-1 disabled:pointer-events-none disabled:opacity-50 font-mono tracking-wide relative overflow-hidden group";

        const variants = {
            primary: "bg-accent-1 text-black hover:bg-accent-1/90 shadow-[0_0_15px_rgba(0,240,255,0.4)] hover:shadow-[0_0_25px_rgba(0,240,255,0.6)]",
            secondary: "bg-accent-2 text-white hover:bg-accent-2/90 shadow-[0_0_15px_rgba(140,78,255,0.4)]",
            outline: "border border-accent-1/30 text-accent-1 hover:bg-accent-1/10 hover:border-accent-1/60",
            ghost: "text-text-primary hover:bg-white/5 hover:text-white",
            neon: "bg-transparent border border-accent-1 text-accent-1 shadow-[0_0_10px_rgba(0,240,255,0.3),inset_0_0_10px_rgba(0,240,255,0.1)] hover:shadow-[0_0_20px_rgba(0,240,255,0.5),inset_0_0_20px_rgba(0,240,255,0.2)] hover:bg-accent-1/10",
        };

        const sizes = {
            sm: "h-8 px-3 text-xs",
            md: "h-10 px-4 py-2",
            lg: "h-12 px-8 text-lg",
            icon: "h-10 w-10",
        };

        return (
            <button
                ref={ref}
                className={cn(baseStyles, variants[variant], sizes[size], className)}
                {...props}
            >
                {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
                {children}
                {/* Subtle glow effect on hover for neon/outline */}
                {(variant === 'neon' || variant === 'outline') && (
                    <span className="absolute inset-0 rounded-md ring-2 ring-white/10 opacity-0 group-hover:opacity-100 transition-opacity" />
                )}
            </button>
        );
    }
);
Button.displayName = 'Button';

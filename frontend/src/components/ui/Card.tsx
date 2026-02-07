import React from 'react';
import { cn } from '@/lib/utils';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
    hoverEffect?: boolean;
}

export const Card = React.forwardRef<HTMLDivElement, CardProps>(
    ({ className, hoverEffect = false, ...props }, ref) => {
        return (
            <div
                ref={ref}
                className={cn(
                    "glass-card rounded-xl p-6 transition-all duration-300",
                    hoverEffect && "hover:translate-y-[-5px] hover:shadow-[0_10px_30px_rgba(0,240,255,0.1)] hover:border-accent-1/40",
                    className
                )}
                {...props}
            />
        );
    }
);
Card.displayName = 'Card';

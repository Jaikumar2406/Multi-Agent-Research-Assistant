import { useState, useEffect } from 'react';
import { useScroll, useTransform } from 'framer-motion';

export function useScrollToFrame(frameCount: number, height: number = 2000) {
    const [currentFrame, setCurrentFrame] = useState(1);
    const { scrollY } = useScroll();

    // Map scrollY from 0 to 'height' -> 1 to frameCount
    const frameIndex = useTransform(scrollY, [0, height], [1, frameCount]);

    useEffect(() => {
        return frameIndex.on("change", (latest) => {
            // Clamp between 1 and frameCount
            const frame = Math.max(1, Math.min(frameCount, Math.round(latest)));
            setCurrentFrame(frame);
        });
    }, [frameIndex, frameCount]);

    return currentFrame;
}

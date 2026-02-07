import { useState, useEffect, useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

import { useScrollToFrame } from '@/hooks/useScrollToFrame';
import { Button } from '@/components/ui/Button';
import { Card } from '@/components/ui/Card';
import { Brain, Network, BarChart3, ArrowRight } from 'lucide-react';

const TOTAL_FRAMES = 196; // Based on file count

export const LandingPage = () => {
    const currentFrame = useScrollToFrame(TOTAL_FRAMES, 3000);
    const [images, setImages] = useState<HTMLImageElement[]>([]);
    const canvasRef = useRef<HTMLCanvasElement>(null);

    // Preload images
    useEffect(() => {
        const loadImages = async () => {
            const loadedImages: HTMLImageElement[] = [];
            for (let i = 1; i <= TOTAL_FRAMES; i++) {
                const img = new Image();
                const frameNumber = i.toString().padStart(3, '0');
                img.src = `/images/ezgif-frame-${frameNumber}.jpg`;
                loadedImages.push(img);
            }
            setImages(loadedImages);
        };
        loadImages();
    }, []);

    // Draw to canvas
    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas || images.length === 0) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const img = images[currentFrame - 1];
        if (img && img.complete) {
            // Handle High-DPI (Retina/4K) displays
            const dpr = window.devicePixelRatio || 1;

            // Set canvas size to physical pixels
            canvas.width = window.innerWidth * dpr;
            canvas.height = window.innerHeight * dpr;

            // Scale context to ensure correct drawing operations if needed
            // For drawImage with cover, we calculate scale based on physical width/height directly

            // Draw image cover style
            const scale = Math.max(canvas.width / img.width, canvas.height / img.height);
            const x = (canvas.width / 2) - (img.width / 2) * scale;
            const y = (canvas.height / 2) - (img.height / 2) * scale;

            ctx.globalAlpha = 1.0; // Full opacity
            ctx.drawImage(img, x, y, img.width * scale, img.height * scale);
        }
    }, [currentFrame, images]);

    const { scrollY } = useScroll();

    // Text 1: Starts visible, fades out
    const opacity1 = useTransform(scrollY, [0, 400], [1, 0]);
    const y1 = useTransform(scrollY, [0, 400], [0, -50]);
    const pointerEvents1 = useTransform(scrollY, (v) => v > 300 ? 'none' : 'auto');

    // Text 2: Fades in middle, then out
    const opacity2 = useTransform(scrollY, [600, 1000, 1400], [0, 1, 0]);
    const y2 = useTransform(scrollY, [600, 1400], [50, -50]);

    // Text 3: Fades in towards end
    const opacity3 = useTransform(scrollY, [1600, 2000, 2400], [0, 1, 0]);
    const y3 = useTransform(scrollY, [1600, 2400], [50, -50]);

    return (
        <div className="relative">
            {/* Hero Section with Moving Canvas */}
            <div className="h-[300vh] relative">
                <div className="sticky top-0 h-screen overflow-hidden">
                    <canvas ref={canvasRef} className="absolute inset-0 w-full h-full object-cover" />

                    {/* Scroll Text overlays */}
                    <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                        {/* Stage 1 */}
                        <motion.div
                            style={{ opacity: opacity1, y: y1, pointerEvents: pointerEvents1 }}
                            className="text-center px-4 absolute"
                        >
                            <h1 className="text-5xl md:text-7xl font-bold mb-6 text-white text-glow drop-shadow-2xl">
                                Unlocking Tomorrow's Insights
                            </h1>
                            <p className="text-xl text-text-primary/80 font-mono bg-black/30 backdrop-blur-sm p-2 rounded inline-block">
                                Scroll to Initialize
                            </p>
                        </motion.div>

                        {/* Stage 2 */}
                        <motion.div
                            style={{ opacity: opacity2, y: y2 }}
                            className="text-center px-4 absolute"
                        >
                            <h2 className="text-4xl md:text-6xl font-bold text-accent-1 text-glow drop-shadow-2xl mb-4">
                                Processing Infinite Streams
                            </h2>
                            <p className="text-xl text-white font-light bg-black/30 backdrop-blur-md p-4 rounded-xl border border-white/10">
                                Synthesizing data points across the quantum grid...
                            </p>
                        </motion.div>

                        {/* Stage 3 */}
                        <motion.div
                            style={{ opacity: opacity3, y: y3 }}
                            className="text-center px-4 absolute"
                        >
                            <h2 className="text-4xl md:text-6xl font-bold text-accent-2 text-glow drop-shadow-2xl mb-6">
                                Insight Achieved
                            </h2>
                            <div className="pointer-events-auto">
                                <Button variant="neon" size="lg" className="animate-pulse-slow">
                                    Begin Research
                                </Button>
                            </div>
                        </motion.div>
                    </div>
                </div>
            </div>

            {/* Features Section */}
            <section className="py-24 px-4 sm:px-6 lg:px-8 relative z-10 bg-background">
                <div className="max-w-7xl mx-auto">
                    <h2 className="text-3xl md:text-4xl font-bold mb-16 text-center text-accent-1">Our Capabilities</h2>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                        <Card hoverEffect className="flex flex-col items-center text-center p-8">
                            <div className="w-16 h-16 rounded-full bg-accent-1/10 flex items-center justify-center mb-6">
                                <Brain className="w-8 h-8 text-accent-1" />
                            </div>
                            <h3 className="text-xl font-bold mb-4 text-white">AI-Powered Synthesis</h3>
                            <p className="text-text-secondary leading-relaxed">
                                Advanced algorithms for rapid data synthesis across diverse sources, extracting key insights in milliseconds.
                            </p>
                        </Card>

                        <Card hoverEffect className="flex flex-col items-center text-center p-8 border-accent-2/30">
                            <div className="w-16 h-16 rounded-full bg-accent-2/10 flex items-center justify-center mb-6">
                                <Network className="w-8 h-8 text-accent-2" />
                            </div>
                            <h3 className="text-xl font-bold mb-4 text-white">Contextual Intelligence</h3>
                            <p className="text-text-secondary leading-relaxed">
                                Understanding nuance, identifying patterns, and drawing intelligent connections between seemingly unrelated data points.
                            </p>
                        </Card>

                        <Card hoverEffect className="flex flex-col items-center text-center p-8">
                            <div className="w-16 h-16 rounded-full bg-accent-1/10 flex items-center justify-center mb-6">
                                <BarChart3 className="w-8 h-8 text-accent-1" />
                            </div>
                            <h3 className="text-xl font-bold mb-4 text-white">Dynamic Visualization</h3>
                            <p className="text-text-secondary leading-relaxed">
                                Transforming complex data into intuitive, interactive visual narratives that tell the story behind the numbers.
                            </p>
                        </Card>
                    </div>
                </div>
            </section>

            {/* Why Choose Section */}
            <section className="py-24 px-4 sm:px-6 lg:px-8 relative z-10 bg-black/40">
                <div className="max-w-7xl mx-auto">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
                        <div>
                            <h2 className="text-3xl md:text-4xl font-bold mb-8 text-white">Why Choose <span className="text-accent-2">Quantum Nexus?</span></h2>
                            <div className="space-y-6">
                                {[
                                    "Real-time data processing with quantum-inspired algorithms.",
                                    "Secure, encrypted knowledge graphs for sensitive research.",
                                    "Generative visualization tailored to your specific domain.",
                                    "Collaborative workspaces with infinite scalability."
                                ].map((item, i) => (
                                    <div key={i} className="flex items-start space-x-4">
                                        <div className="mt-1 w-6 h-6 rounded-full bg-accent-2/20 flex items-center justify-center flex-shrink-0">
                                            <ArrowRight className="w-4 h-4 text-accent-2" />
                                        </div>
                                        <p className="text-lg text-text-primary">{item}</p>
                                    </div>
                                ))}
                            </div>
                            <Button variant="primary" className="mt-10">
                                Explore the Platform
                            </Button>
                        </div>
                        <div className="relative">
                            <div className="absolute inset-0 bg-accent-2/20 blur-3xl rounded-full" />
                            <Card className="relative z-10 aspect-square flex items-center justify-center overflow-hidden border-accent-2/50">
                                {/* Abstract visual placeholder */}
                                <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-accent-2/10 via-black to-black" />
                                <div className="text-center p-8 relative z-20">
                                    <p className="text-6xl font-mono font-bold text-accent-2 mb-2">99.9%</p>
                                    <p className="text-xl text-text-secondary">Accuracy in Data Synthesis</p>
                                </div>
                            </Card>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

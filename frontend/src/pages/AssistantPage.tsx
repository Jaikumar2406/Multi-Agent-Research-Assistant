import React, { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/Button';
import { Input } from '@/components/ui/Input';
import { Card } from '@/components/ui/Card';
import { Send, FileText, Share2, Database, Terminal as TerminalIcon } from 'lucide-react';

export const AssistantPage = () => {
    const [messages, setMessages] = useState<{ role: 'user' | 'system', content: string }[]>([
        { role: 'system', content: 'Quantum Nexus Terminal via Secure Uplink...' },
        { role: 'system', content: 'System initialized. Ready for research query.' }
    ]);
    const [input, setInput] = useState('');
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    // Generate a simple session ID for the thread
    const [threadId] = useState(() => Math.random().toString(36).substring(7));
    const [iteration, setIteration] = useState(0);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMessage = input;
        setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
        setInput('');

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: userMessage,
                    thread_id: threadId,
                    iteration: iteration
                }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            const data = await response.json();
            // Backend returns: { thread_id: str, reply: str, iteration: int }
            const aiResponse = data.reply || JSON.stringify(data);

            // Update iteration from backend, or increment locally
            if (typeof data.iteration === 'number') {
                setIteration(data.iteration);
            } else {
                setIteration(prev => prev + 1);
            }

            setMessages(prev => [...prev, { role: 'system', content: aiResponse }]);

        } catch (error) {
            console.error('Failed to fetch chat response:', error);
            let errorMessage = 'Error: Failed to connect to Quantum Nexus backend.';
            if (error instanceof Error) {
                errorMessage += ` (${error.message})`;
            }
            setMessages(prev => [...prev, { role: 'system', content: errorMessage }]);
        }
    };

    return (
        <div className="h-[calc(100vh-4rem)] flex overflow-hidden">
            {/* Left Sidebar - Knowledge Graph */}
            <aside className="w-64 glass border-r border-white/5 hidden md:flex flex-col p-4">
                <h2 className="text-sm font-bold text-accent-2 mb-4 uppercase tracking-widest flex items-center">
                    <Share2 className="w-4 h-4 mr-2" />
                    Knowledge Graph
                </h2>
                <div className="flex-grow relative rounded-lg bg-black/40 border border-white/5 overflow-hidden p-2">
                    {/* Abstract visual representation of nodes */}
                    <div className="absolute top-1/2 left-1/2 w-2 h-2 bg-accent-1 rounded-full shadow-[0_0_10px_#00F0FF]" />
                    <div className="absolute top-1/4 left-1/4 w-1.5 h-1.5 bg-accent-2 rounded-full animate-pulse" />
                    <div className="absolute bottom-1/3 right-1/4 w-1.5 h-1.5 bg-white rounded-full animate-pulse-slow" />
                    <svg className="absolute inset-0 w-full h-full pointer-events-none opacity-30">
                        <line x1="50%" y1="50%" x2="25%" y2="25%" stroke="#00F0FF" strokeWidth="0.5" />
                        <line x1="50%" y1="50%" x2="75%" y2="66%" stroke="#8C4EFF" strokeWidth="0.5" />
                    </svg>
                    <div className="text-xs text-text-secondary mt-auto">
                        Nodes: Active
                        <br />
                        Connections: 12,403
                    </div>
                </div>
            </aside>

            {/* Main Terminal Area */}
            <main className="flex-1 flex flex-col relative bg-black/20">
                <div className="flex-1 overflow-y-auto p-6 space-y-4 scrollbar-thin scrollbar-thumb-accent-1/20 scrollbar-track-transparent">
                    {messages.map((msg, idx) => (
                        <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                            <div className={`max-w-2xl p-4 rounded-lg font-mono text-sm ${msg.role === 'user'
                                ? 'bg-accent-1/10 border border-accent-1/30 text-text-primary'
                                : 'bg-black/40 border border-white/10 text-data'
                                }`}>
                                {msg.role === 'system' && <TerminalIcon className="w-3 h-3 mb-2 opacity-50" />}
                                {msg.content}
                            </div>
                        </div>
                    ))}
                    <div ref={messagesEndRef} />
                </div>

                <div className="p-4 glass border-t border-white/10">
                    <form onSubmit={handleSubmit} className="flex gap-4">
                        <Input
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            placeholder="Enter research parameters..."
                            className="flex-1 bg-black/50 border-accent-1/30 focus:ring-accent-1/50"
                        />
                        <Button type="submit" variant="neon" size="icon">
                            <Send className="w-4 h-4" />
                        </Button>
                    </form>
                </div>
            </main>

            {/* Right Sidebar - Sources */}
            <aside className="w-72 glass border-l border-white/5 hidden lg:flex flex-col p-4">
                <h2 className="text-sm font-bold text-accent-1 mb-4 uppercase tracking-widest flex items-center">
                    <Database className="w-4 h-4 mr-2" />
                    Sources & Citations
                </h2>
                <div className="space-y-3 overflow-y-auto pr-2">
                    {[1, 2, 3, 4, 5].map((i) => (
                        <Card key={i} className="p-3 bg-black/40 hover:bg-white/5 border-white/5 cursor-pointer text-xs">
                            <div className="flex items-start justify-between mb-1">
                                <span className="text-accent-1 font-mono">REF-{2024 + i}</span>
                                <FileText className="w-3 h-3 text-text-secondary" />
                            </div>
                            <p className="text-text-primary mb-1 line-clamp-2">
                                "Quantum Entanglement in Macroscopic Biological Systems: A Review"
                            </p>
                            <div className="text-text-secondary text-[10px]">
                                Journal of Adv. Physics • 2024
                            </div>
                        </Card>
                    ))}
                </div>
            </aside>
        </div>
    );
};

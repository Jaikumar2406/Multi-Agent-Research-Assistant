import { Button } from '@/components/ui/Button';
import { Input } from '@/components/ui/Input';
import { Card } from '@/components/ui/Card';
import { Mail, MessageSquare, Radio } from 'lucide-react';

export const ContactPage = () => {
    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 relative">
            {/* Background stars effect could be added here specifically if needed */}

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div>
                    <div className="mb-8">
                        <h1 className="text-4xl font-bold mb-4 text-white">Secure Uplink</h1>
                        <p className="text-text-secondary">
                            Establish a direct encrypted connection with our support cadre.
                        </p>
                    </div>

                    <Card className="border-accent-1/20 bg-black/40 p-8 space-y-6">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div className="space-y-2">
                                <label className="text-xs font-mono text-text-secondary uppercase">Identity</label>
                                <Input placeholder="Dr. Freeman" className="bg-black/30" />
                            </div>
                            <div className="space-y-2">
                                <label className="text-xs font-mono text-text-secondary uppercase">Frequency (Email)</label>
                                <Input placeholder="freeman@blackmesa.org" className="bg-black/30" />
                            </div>
                        </div>
                        <div className="space-y-2">
                            <label className="text-xs font-mono text-text-secondary uppercase">Subject Parameter</label>
                            <Input placeholder="Anomaly Detection" className="bg-black/30" />
                        </div>
                        <div className="space-y-2">
                            <label className="text-xs font-mono text-text-secondary uppercase">Transmission</label>
                            <textarea
                                className="flex min-h-[120px] w-full rounded-md border border-white/10 bg-black/30 px-3 py-2 text-sm text-text-primary placeholder:text-text-secondary focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-accent-1 focus-visible:border-accent-1/50 disabled:cursor-not-allowed disabled:opacity-50 font-mono transition-all"
                                placeholder="Enter your query..."
                            />
                        </div>
                        <Button variant="primary" className="w-full">
                            Initiate Transmission
                        </Button>
                    </Card>
                </div>

                <div className="space-y-8">
                    <Card className="p-6 flex items-start space-x-4 border-accent-2/30">
                        <div className="p-3 rounded-full bg-accent-2/10">
                            <Mail className="w-6 h-6 text-accent-2" />
                        </div>
                        <div>
                            <h3 className="font-bold text-white mb-1">Direct Feed</h3>
                            <p className="text-text-secondary text-sm">uplink@quantumnexus.ai</p>
                        </div>
                    </Card>

                    <Card className="p-6 flex items-start space-x-4 border-accent-1/30">
                        <div className="p-3 rounded-full bg-accent-1/10">
                            <Radio className="w-6 h-6 text-accent-1 animate-pulse" />
                        </div>
                        <div>
                            <h3 className="font-bold text-white mb-1">Live Support</h3>
                            <p className="text-text-secondary text-sm">Available 24/7 on secure channels.</p>
                        </div>
                    </Card>

                    <div className="relative h-64 rounded-xl overflow-hidden glass border border-white/5 flex items-center justify-center">
                        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-accent-1/20 via-black to-black opacity-50" />
                        <div className="text-center relative z-10">
                            <MessageSquare className="w-12 h-12 text-white/20 mx-auto mb-4" />
                            <p className="text-text-secondary text-xs font-mono">ENCRYPTED // NO SIGNAL LOSS</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

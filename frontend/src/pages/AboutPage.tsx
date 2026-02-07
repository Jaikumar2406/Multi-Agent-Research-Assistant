import { Card } from '@/components/ui/Card';

export const AboutPage = () => {
    const timeline = [
        { year: '2020', title: 'Inception', desc: 'The Quantum Nexus protocol was initiated to bridge the gap between AI and human intuition.' },
        { year: '2022', title: 'First Singularity', desc: 'Achieved 99% accuracy in predictive synthesis models.' },
        { year: '2024', title: 'Global Grid', desc: 'Expanded the research network to 150+ universities and private labs.' },
        { year: '2026', title: 'Nexus Prime', desc: 'Launch of the fully autonomous research assistant interface.' },
    ];

    const team = [
        { name: 'Dr. Astra Vance', role: 'Chief Scientist', image: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?fit=crop&w=200&h=200' },
        { name: 'Marcus Thorne', role: 'Lead Architect', image: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?fit=crop&w=200&h=200' },
        { name: 'Elena Kho', role: 'Quantum Systems', image: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?fit=crop&w=200&h=200' },
        { name: 'David Chen', role: 'Data Visualization', image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?fit=crop&w=200&h=200' },
    ];

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">

            <div className="mb-20 text-center">
                <h1 className="text-4xl font-bold mb-4 text-white">Our Origin Protocol</h1>
                <p className="text-text-secondary max-w-2xl mx-auto">
                    Tracing the evolution of intelligence from inception to the infinite.
                </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
                {/* Timeline */}
                <div>
                    <h2 className="text-2xl font-mono font-bold text-accent-1 mb-8">System Logs</h2>
                    <div className="space-y-8 relative border-l border-white/10 pl-8 ml-4">
                        {timeline.map((item, idx) => (
                            <div key={idx} className="relative">
                                <span className="absolute -left-[39px] top-1 w-4 h-4 rounded-full bg-background border-2 border-accent-2" />
                                <div className="flex flex-col sm:flex-row sm:items-baseline mb-2">
                                    <span className="text-xl font-mono font-bold text-accent-2 mr-4">{item.year}</span>
                                    <h3 className="text-lg font-bold text-white">{item.title}</h3>
                                </div>
                                <p className="text-text-secondary">{item.desc}</p>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Team */}
                <div>
                    <h2 className="text-2xl font-mono font-bold text-accent-1 mb-8">The Cadre</h2>
                    <div className="grid grid-cols-2 md:grid-cols-2 gap-6">
                        {team.map((member, idx) => (
                            <Card key={idx} className="p-4 flex flex-col items-center text-center border-white/5 hover:border-accent-1/30 transition-colors">
                                <div className="w-24 h-24 rounded-full overflow-hidden mb-4 ring-2 ring-accent-1/50 shadow-[0_0_15px_rgba(0,240,255,0.3)]">
                                    <img src={member.image} alt={member.name} className="w-full h-full object-cover" />
                                </div>
                                <h3 className="font-bold text-white font-mono">{member.name}</h3>
                                <p className="text-xs text-text-secondary mt-1 uppercase tracking-wider">{member.role}</p>
                            </Card>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default function ThinkingBubble() {

    return (

        <div className="flex justify-start">

            <div
                className="
                    max-w-xl
                    rounded-3xl
                    border
                    border-slate-700
                    bg-slate-900
                    px-6
                    py-5
                    shadow-xl
                "
            >

                <div className="mb-4 text-xs uppercase tracking-widest text-blue-400">

                    🏎 ApexIQ

                </div>

                <div className="space-y-4 text-slate-300">

                    <LoadingLine text="Searching FIA Regulations..." />

                    <LoadingLine text="Ranking semantic matches..." />

                    <LoadingLine text="Generating grounded answer..." />

                </div>

            </div>

        </div>

    );

}

function LoadingLine({ text }: { text: string }) {

    return (

        <div className="flex items-center gap-3">

            <span className="flex gap-1">

                <span
                    className="
                        h-2
                        w-2
                        rounded-full
                        bg-blue-500
                        animate-bounce
                    "
                />

                <span
                    className="
                        h-2
                        w-2
                        rounded-full
                        bg-blue-500
                        animate-bounce
                        [animation-delay:150ms]
                    "
                />

                <span
                    className="
                        h-2
                        w-2
                        rounded-full
                        bg-blue-500
                        animate-bounce
                        [animation-delay:300ms]
                    "
                />

            </span>

            <span>{text}</span>

        </div>

    );

}
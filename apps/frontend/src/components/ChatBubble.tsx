import type { ChatMessage } from "../types/chat";
import SourceCard from "./SourceCard";

interface Props {
    message: ChatMessage;
}

export default function ChatBubble({ message }: Props) {

    const isUser = message.role === "user";

    return (

        <div
            className={`flex ${
                isUser ? "justify-end" : "justify-start"
            }`}
        >

            <div
                className={`
                    max-w-3xl
                    rounded-2xl
                    px-6
                    py-5
                    shadow-lg
                    whitespace-pre-wrap
                    transition-all
                    duration-300

                    ${
                        isUser
                            ? "bg-blue-600 text-white"
                            : "border border-slate-700 bg-slate-900 text-slate-300"
                    }
                `}
            >

                <div className="mb-3 text-sm font-semibold opacity-70">

                    {isUser ? "You" : "🏎 ApexIQ"}

                </div>

                <div>

                    {message.content}

                    {message.sources && message.sources.length > 0 && (

                        <>

                            <hr className="my-6 border-slate-700" />

                            <h3 className="mb-4 font-semibold text-slate-300">

                                Sources

                            </h3>

                            <div className="space-y-3">

                                {message.sources.map((source, index) => (

                                    <SourceCard
                                        key={index}
                                        source={source}
                                    />

                                ))}

                            </div>

                        </>

                    )}

                </div>

            </div>

        </div>

    );

}
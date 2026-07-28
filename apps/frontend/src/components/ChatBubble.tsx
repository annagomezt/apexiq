import { useState } from "react";

import ReactMarkdown from "react-markdown";

import type { ChatMessage } from "../types/chat";
import SourceCard from "./SourceCard";

interface Props {
    message: ChatMessage;
}

export default function ChatBubble({ message }: Props) {

    const isUser = message.role === "user";

    const [copied, setCopied] = useState(false);

    async function copyAnswer() {

        await navigator.clipboard.writeText(message.content);

        setCopied(true);

        setTimeout(() => {

            setCopied(false);

        }, 2000);

    }

    return (

        <div
            className={`flex ${
                isUser ? "justify-end" : "justify-start"
            }`}
        >

            <div
                className={`
                    max-w-3xl
                    rounded-3xl
                    px-6
                    py-5
                    shadow-xl
                    transition-all
                    duration-300

                    ${
                        isUser
                            ? "bg-blue-600 text-white"
                            : "border border-slate-700 bg-slate-900"
                    }
                `}
            >

                <div
                    className={`
                        mb-4
                        flex
                        items-center
                        justify-between

                        text-xs
                        uppercase
                        tracking-widest

                        ${
                            isUser
                                ? "text-blue-100"
                                : "text-blue-400"
                        }
                    `}
                >

                    <span>

                        {isUser ? "You" : "🏎 ApexIQ"}

                    </span>

                    {

                        !isUser &&

                        <button

                            onClick={copyAnswer}

                            className="
                                rounded-lg
                                bg-slate-800
                                px-3
                                py-1
                                text-[11px]
                                font-medium
                                transition
                                hover:bg-slate-700
                            "

                        >

                            {copied ? "Copied!" : "Copy"}

                        </button>

                    }

                </div>

                <div
                    className={`
                        prose
                        prose-invert
                        max-w-none

                        ${
                            isUser
                                ? "text-white"
                                : "text-slate-300"
                        }
                    `}
                >

                    <ReactMarkdown>

                        {message.content}

                    </ReactMarkdown>

                </div>

                {

                    !isUser &&
                    message.sources &&
                    message.sources.length > 0 &&

                    <>

                        <div className="my-6 h-px bg-slate-700" />

                        <h3 className="mb-3 text-sm font-semibold text-slate-400">

                            References

                        </h3>

                        <div className="grid gap-4">

                            {

                                message.sources.map((source, index) => (

                                    <SourceCard

                                        key={index}

                                        source={source}

                                    />

                                ))

                            }

                        </div>

                    </>

                }

            </div>

        </div>

    );

}
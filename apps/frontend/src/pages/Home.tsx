import { useEffect, useRef, useState } from "react";

import Sidebar from "../components/sidebar/Sidebar";
import ChatInput from "../components/ChatInput";
import ChatBubble from "../components/ChatBubble";
import ThinkingBubble from "../components/ThinkingBubble";

import type { ChatMessage } from "../types/chat";
import type { Conversation } from "../types/conversation";

export default function Home() {

    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [loading, setLoading] = useState(false);

    const messagesEndRef = useRef<HTMLDivElement>(null);

    useEffect(() => {

        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth",
        });

    }, [messages, loading]);

    function handleNewChat() {

        setMessages([]);
        setLoading(false);

    }

    function handleSelectConversation(id: number) {

        console.log("Conversation:", id);

    }

    const conversations: Conversation[] = [

        {

            id: 1,

            title: "Current Chat",

            messages,

        },

    ];

    async function handleSend(question: string) {

        const userMessage: ChatMessage = {
            role: "user",
            content: question,
        };

        setMessages((old) => [...old, userMessage]);

        setLoading(true);

        try {

            const response = await fetch("http://127.0.0.1:8000/chat", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                },

                body: JSON.stringify({
                    question,
                }),

            });

            const data = await response.json();

            const assistantMessage: ChatMessage = {
                role: "assistant",
                content: data.answer,
                sources: data.sources,
            };

            setMessages((old) => [...old, assistantMessage]);

        }

        catch (error) {

            console.error(error);

            setMessages((old) => [

                ...old,

                {

                    role: "assistant",

                    content: "Error connecting to ApexIQ API.",

                },

            ]);

        }

        setLoading(false);

    }

    return (

        <main className="flex h-screen bg-slate-950 text-white">

            <Sidebar

                conversations={conversations}

                currentId={1}

                onSelect={handleSelectConversation}

                onNewChat={handleNewChat}

            />

            <section className="flex flex-1 flex-col">

                <header
                    className="
                        flex
                        items-center
                        justify-between
                        border-b
                        border-slate-800
                        px-10
                        py-8
                    "
                >

                    <div>

                        <h1 className="text-4xl font-bold">

                            ApexIQ

                        </h1>

                        <p className="mt-2 text-slate-400">

                            Ask anything about FIA Regulations.

                        </p>

                    </div>

                    <button

                        onClick={handleNewChat}

                        disabled={messages.length === 0}

                        className="
                            rounded-xl
                            border
                            border-red-500
                            px-5
                            py-2
                            text-red-400
                            transition

                            hover:bg-red-500
                            hover:text-white

                            disabled:cursor-not-allowed
                            disabled:opacity-40
                        "

                    >

                        Clear Chat

                    </button>

                </header>

                <div
                    className="
                        flex-1
                        overflow-y-auto
                        px-10
                        py-8
                    "
                >

                    <div className="mx-auto flex max-w-4xl flex-col gap-6">

                        {

                            messages.length === 0 && (

                                <div className="mt-24 text-center">

                                    <h2 className="text-5xl font-bold">

                                        Welcome to ApexIQ

                                    </h2>

                                    <p className="mt-5 text-lg text-slate-400">

                                        Ask anything about Formula 1 FIA Regulations.

                                    </p>

                                </div>

                            )

                        }

                        {

                            messages.map((message, index) => (

                                <ChatBubble

                                    key={index}

                                    message={message}

                                />

                            ))

                        }

                        {

                            loading && <ThinkingBubble />

                        }

                        <div ref={messagesEndRef} />

                    </div>

                </div>

                <footer
                    className="
                        border-t
                        border-slate-800
                        px-10
                        py-6
                    "
                >

                    <div className="mx-auto max-w-4xl">

                        <ChatInput onSend={handleSend} />

                    </div>

                </footer>

            </section>

        </main>

    );

}
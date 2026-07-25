import { useState } from "react";

import ChatInput from "../components/ChatInput";
import ChatBubble from "../components/ChatBubble";

import type { ChatMessage } from "../types/chat";

export default function Home() {

    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [loading, setLoading] = useState(false);

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

        } catch (error) {

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

        <main className="min-h-screen bg-slate-950 text-white">

            <section className="mx-auto flex max-w-5xl flex-col px-8 py-16">

                <h1 className="text-center text-6xl font-bold">

                    ApexIQ

                </h1>

                <p className="mx-auto mt-6 max-w-2xl text-center text-lg text-slate-400">

                    Ask anything about FIA regulations.

                    ApexIQ searches official FIA documents using AI and answers with grounded sources.

                </p>

                <div className="mt-16 flex flex-col gap-6">

                    {messages.map((message, index) => (

                        <ChatBubble
                            key={index}
                            message={message}
                        />

                    ))}

                    {loading && (

                        <div className="flex justify-start">

                            <div
                                className="
                                    rounded-2xl
                                    border
                                    border-slate-700
                                    bg-slate-900
                                    px-5
                                    py-4
                                    text-slate-400
                                "
                            >

                                ApexIQ is thinking...

                            </div>

                        </div>

                    )}

                </div>

                <div className="mt-10">

                    <ChatInput onSend={handleSend} />

                </div>

            </section>

        </main>

    );

}
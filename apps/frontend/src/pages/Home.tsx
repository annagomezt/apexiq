import { useState } from "react";

import ChatInput from "../components/ChatInput";

export default function Home() {

    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleSend(question: string) {

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

            setAnswer(data.answer);

        } catch (error) {

            console.error(error);

            setAnswer("Error connecting to ApexIQ API.");

        }

        setLoading(false);

    }

    return (

        <main className="min-h-screen bg-slate-950 text-white">

            <section className="mx-auto flex max-w-5xl flex-col items-center justify-center px-8 py-20">

                <h1 className="text-center text-6xl font-bold">
                    ApexIQ
                </h1>

                <p className="mt-6 max-w-2xl text-center text-lg text-slate-400">

                    Ask anything about FIA regulations.

                    ApexIQ searches official FIA documents using AI and answers with grounded sources.

                </p>

                <ChatInput onSend={handleSend} />

                {loading && (

                    <div className="mt-10 text-slate-400">
                        Thinking...
                    </div>

                )}

                {!loading && answer && (

                    <div
                        className="
                            mt-10
                            w-full
                            rounded-2xl
                            border
                            border-slate-700
                            bg-slate-900
                            p-8
                        "
                    >

                        <h2 className="mb-4 text-xl font-semibold">

                            Answer

                        </h2>

                        <p className="whitespace-pre-wrap text-slate-300">

                            {answer}

                        </p>

                    </div>

                )}

            </section>

        </main>

    );

}
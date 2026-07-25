import { useState } from "react";

interface Props {
    onSend: (question: string) => void;
}

export default function ChatInput({ onSend }: Props) {

    const [question, setQuestion] = useState("");

    function handleSubmit() {

        if (!question.trim()) return;

        onSend(question);

        setQuestion("");

    }

    return (

        <div className="mt-12 flex w-full max-w-3xl gap-3">

            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        handleSubmit();
                    }
                }}
                placeholder="Ask anything about FIA Regulations..."
                className="
                    flex-1
                    rounded-xl
                    border
                    border-slate-700
                    bg-slate-900
                    px-5
                    py-4
                    text-white
                    outline-none
                    focus:border-blue-500
                "
            />

            <button
                onClick={handleSubmit}
                className="
                    rounded-xl
                    bg-blue-600
                    px-8
                    font-semibold
                    text-white
                    transition
                    hover:bg-blue-500
                "
            >
                Ask
            </button>

        </div>

    );

}
import { useEffect, useRef, useState } from "react";

interface Props {
    onSend: (question: string) => void;
}

export default function ChatInput({ onSend }: Props) {

    const [question, setQuestion] = useState("");

    const textareaRef = useRef<HTMLTextAreaElement>(null);

    useEffect(() => {

        textareaRef.current?.focus();

    }, []);

    useEffect(() => {

        if (!textareaRef.current) return;

        textareaRef.current.style.height = "0px";

        textareaRef.current.style.height =
            textareaRef.current.scrollHeight + "px";

    }, [question]);

    function handleSubmit() {

        if (!question.trim()) return;

        onSend(question.trim());

        setQuestion("");

        textareaRef.current?.focus();

    }

    return (

        <div
            className="
                w-full
                rounded-3xl
                border
                border-slate-700
                bg-slate-900
                p-3
                shadow-xl
            "
        >

            <div className="flex items-end gap-3">

                <textarea

                    ref={textareaRef}

                    rows={1}

                    value={question}

                    onChange={(e) => setQuestion(e.target.value)}

                    onKeyDown={(e) => {

                        if (e.key === "Enter" && !e.shiftKey) {

                            e.preventDefault();

                            handleSubmit();

                        }

                    }}

                    placeholder="Ask anything about FIA regulations..."

                    className="
                        max-h-52
                        min-h-7
                        flex-1
                        resize-none
                        overflow-y-auto
                        bg-transparent
                        px-2
                        py-2
                        text-white
                        outline-none
                        placeholder:text-slate-500
                    "

                />

                <button

                    onClick={handleSubmit}

                    className="
                        rounded-2xl
                        bg-blue-600
                        px-5
                        py-3
                        font-semibold
                        text-white
                        transition-all
                        duration-200
                        hover:scale-105
                        hover:bg-blue-500
                        active:scale-95
                    "

                >

                    Send

                </button>

            </div>

        </div>

    );

}
import type { Conversation } from "../../types/conversation";

interface Props {

    conversations: Conversation[];

    currentId: number;

    onSelect: (id: number) => void;

    onNewChat: () => void;

}

export default function Sidebar({

    conversations,

    currentId,

    onSelect,

    onNewChat,

}: Props) {

    return (

        <aside
            className="
                flex
                w-72
                flex-col
                border-r
                border-slate-800
                bg-slate-950
                p-6
            "
        >

            <h1 className="text-3xl font-bold">

                ApexIQ

            </h1>

            <p className="mt-2 text-sm text-slate-500">

                FIA Regulation Assistant

            </p>

            <button

                onClick={onNewChat}

                className="
                    mt-10
                    rounded-xl
                    bg-blue-600
                    py-3
                    font-semibold
                    transition
                    hover:bg-blue-500
                "

            >

                + New Chat

            </button>

            <div className="mt-10">

                <p className="mb-4 text-xs uppercase tracking-wider text-slate-500">

                    Conversations

                </p>

                <div className="space-y-2">

                    {

                        conversations.map((conversation) => (

                            <button

                                key={conversation.id}

                                onClick={() => onSelect(conversation.id)}

                                className={`
                                    w-full
                                    rounded-xl
                                    p-3
                                    text-left
                                    transition

                                    ${
                                        conversation.id === currentId

                                            ? "bg-blue-600"

                                            : "bg-slate-900 hover:bg-slate-800"

                                    }
                                `}

                            >

                                <div className="truncate">

                                    {conversation.title}

                                </div>

                            </button>

                        ))

                    }

                </div>

            </div>

        </aside>

    );

}
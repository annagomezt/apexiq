interface Props {
    source: any;
}

export default function SourceCard({ source }: Props) {

    const metadata = source.metadata;

    const similarity = Math.max(
        0,
        Math.round((1 - source.distance) * 100)
    );

    return (

        <div
            className="
                rounded-2xl
                border
                border-slate-700
                bg-slate-950
                p-5
                transition-all
                duration-300
                hover:border-blue-500
                hover:shadow-lg
                hover:shadow-blue-900/20
            "
        >

            <div className="flex items-center justify-between">

                <div className="flex items-center gap-3">

                    <span className="text-2xl">
                        📘
                    </span>

                    <div>

                        <h3 className="font-semibold text-white">

                            FIA Regulations

                        </h3>

                        <p className="text-sm text-slate-400">

                            {metadata.section}

                        </p>

                    </div>

                </div>

                <span
                    className="
                        rounded-full
                        bg-blue-600/20
                        px-3
                        py-1
                        text-xs
                        font-semibold
                        text-blue-300
                    "
                >

                    {similarity}% match

                </span>

            </div>

            <div className="mt-5 grid grid-cols-2 gap-4">

                <div>

                    <p className="text-xs uppercase tracking-widest text-slate-500">

                        Article

                    </p>

                    <p className="mt-1 font-semibold text-white">

                        {metadata.regulation_id}

                    </p>

                </div>

                <div>

                    <p className="text-xs uppercase tracking-widest text-slate-500">

                        Page

                    </p>

                    <p className="mt-1 font-semibold text-white">

                        {metadata.page}

                    </p>

                </div>

            </div>

            <div className="mt-5">

                <p className="text-xs uppercase tracking-widest text-slate-500">

                    Title

                </p>

                <p className="mt-2 text-slate-300">

                    {metadata.title}

                </p>

            </div>

            <div className="mt-5">

                <p className="text-xs uppercase tracking-widest text-slate-500">

                    Preview

                </p>

                <p className="mt-2 line-clamp-4 text-sm leading-6 text-slate-400">

                    {metadata.text}

                </p>

            </div>

        </div>

    );

}
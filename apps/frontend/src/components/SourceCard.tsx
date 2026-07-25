interface Source {

    distance: number;

    metadata: {

        regulation_id: string;
        title: string;
        source: string;
        page: number;

    };

}

interface Props {

    source: Source;

}

export default function SourceCard({ source }: Props) {

    return (

        <div
            className="
                rounded-xl
                border
                border-slate-700
                bg-slate-950
                p-4
            "
        >

            <div className="font-semibold text-white">

                {source.metadata.title}

            </div>

            <div className="mt-2 text-sm text-slate-400">

                Regulation:
                <span className="ml-2 text-blue-400">

                    {source.metadata.regulation_id}

                </span>

            </div>

            <div className="text-sm text-slate-400">

                Page {source.metadata.page}

            </div>

        </div>

    );

}
interface Props {

    title: string;

    value: string | number;

}

export default function StatCard({

    title,

    value,

}: Props) {

    return (

        <div
            className="
                rounded-xl
                border
                border-slate-700
                bg-slate-950
                p-5
            "
        >

            <p
                className="
                    text-xs
                    uppercase
                    tracking-widest
                    text-slate-500
                "
            >

                {title}

            </p>

            <p
                className="
                    mt-3
                    text-xl
                    font-bold
                    text-white
                "
            >

                {value}

            </p>

        </div>

    );

}
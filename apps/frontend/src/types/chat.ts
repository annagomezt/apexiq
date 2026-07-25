export interface Source {
    distance: number;
    metadata: {
        championship: string;
        section: string;
        regulation_id: string;
        title: string;
        source: string;
        page: number;
        chunk_index: number;
        text: string;
    };
}

export interface ChatResponse {
    question: string;
    answer: string;
    sources: Source[];
}
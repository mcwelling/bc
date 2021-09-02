export type BallotConfig = {
    id: number;
    proposal: string;
    options: string[];
    selected: string};

export type updateData = {
    index: number;
    data: BallotConfig;};
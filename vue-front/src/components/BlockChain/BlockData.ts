export type BlockData = {
    id: number;
    parenthash: string;
    data: string;
    nonce: number;
    blockhash: string;
    valid: boolean};

export type updateMsg = {
    index: number;
    blockhash: string;};
export type BlockData = {
    id: number;
    blockid: string;
    parenthash: string;
    data: string;
    nonce: string;
    blockhash: string;
    valid: boolean};

export type updateMsg = {
    index: number;
    blockhash: string;};
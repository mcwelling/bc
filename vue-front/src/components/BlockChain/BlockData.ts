export type BlockData = {
    id: string;
    blockid: string;
    parenthash: string;
    data: string;
    nonce: string;
    blockhash: string;
    valid: boolean};

export type updateMsg = {
    index: number;
    blockhash: string;};

export type getResponse = {
    constant: string;
    voter_id: string;
    parent_hash: string;
    ballot: string;
    block_hash: string;
    timestamp: string;
    };
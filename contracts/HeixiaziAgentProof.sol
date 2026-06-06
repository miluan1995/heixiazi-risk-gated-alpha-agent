// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title HeixiaziAgentProof
/// @notice Minimal hackathon proof contract for Heixiazi Risk-Gated Alpha Agent.
/// It records auditable agent demo/report hashes on BSC/opBNB testnet or mainnet.
/// It does not custody user funds, trade assets, or grant token approvals.
contract HeixiaziAgentProof {
    struct Proof {
        bytes32 reportHash;
        string uri;
        uint256 createdAt;
    }

    address public immutable owner;
    uint256 public proofCount;
    mapping(uint256 => Proof) public proofs;

    event ProofRecorded(uint256 indexed id, bytes32 indexed reportHash, string uri, uint256 createdAt);

    error NotOwner();

    constructor() {
        owner = msg.sender;
    }

    function recordProof(bytes32 reportHash, string calldata uri) external returns (uint256 id) {
        // Open recording is intentional: judges/users can record their own reproductions.
        id = ++proofCount;
        proofs[id] = Proof({reportHash: reportHash, uri: uri, createdAt: block.timestamp});
        emit ProofRecorded(id, reportHash, uri, block.timestamp);
    }
}

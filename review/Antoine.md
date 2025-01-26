[§1] I only skimmed this chapter but it seems good and appropriate

[§1.3] This needs to be expanded with some concrete numbers (size of proof, prover time, verifier time, etc.)

[§2] Again, just skimmed but seems to cover the right concepts

[§3] The polynomial encodes a trace of the circuit (every wire value from inputs to intermediary values to output)

[§3] Avoid point form, describe in paragraph for a thesis (or a table). Make sure every symbol is defined and defined before it is used

[§3.1] "proofs for multiple blocks" what does block mean in this context?

[§3.1] "proof time of the second circuit grows linearly" The main problem, I think, is that verifying a proof is a complicated circuit to create. The circuit itself is the exponent of the crypto, but the proof is in one the curve and requires curve operations (plus a bilinear pairing) all implemented in at the circuit level

[§3.2] "an improvement from the previous technique" I think the other idea is that you don't have to redo a trusted setup once you figure out the size of what is being proven. 

[§3.3] "the exponential growth of recursion proofs" What is this? This whole section is too short and it is not clear how to relates to IVC. Expand a bit and maybe a diagram will help?

[§3.3.1] Should this be in chapter 2? think about 

[§3.3.1] "it is impossible" it is computationally infeasible.

[§3.3.1] "also much shorter" generally constant size

[§3.3.1] "Instead of committing to a full dataset" I didn't get what this means

[§3.3.1] "Committing to the coefficients of the polynomial directly" Maybe, maybe not, depends on the scheme. Basically you want to say that commits give you BOTH the option to open the entire polynomial or open at a specific eval point

[§3.3.1] KZG setup is universal (done once and useable by anyone; has been done before, like by the ethereum foundation) which is important to mention. it is constant size while bullet proofs are bigger than KZG (logarithmic) but not trusted setup. FRI is post-quantum.. 

[§3.3.2] "the polynomial f1 and its commitment c1." It wasn't clear what you mean here. Opening the entire polynomial? Or at certain points?

[§3.3.2] "additively homomorphic" I don't remember you defining this before, which you should (with an example). My suggestion is at the end of KZG, bulletproofs, fri, you just say from now one we will just talk about KZG and then explain it (additively homomorphic) in the context of KZG. PS if you want to look at this, it might help too: https://plonkbook.org/docs/background/kzg/

[§3.4] "Instead of accumulating the hard part at the end, the folding scheme accumulates everything up until the end." Not clear enough

[§3.4.1] More details of the explanation between each attempt. More justification about why a "relaxed" is "good enough"




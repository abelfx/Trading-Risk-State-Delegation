# Dynamic Forex Risk Constraint System

### 1. What is the domain? 
The domain (Q) represents hierarchical risk states for an automated Forex trading environment. The states, in order of increasing risk, are: `halted` < `observe_only` < `paper_trade` < `micro_lot` < `full_risk`.

### 2. What does ⊗ model in this domain?
The combination operation (⊗) represents the interaction between two systems (e.g., an algorithm's requested risk level and the account's hardcoded risk level). It acts as a strict "meet" (minimum) operator, ensuring the combined effective state is always the strictest of the two constraints. 

### 3. What question does the right residual answer in this domain?
The right residual (a → c) performs backward constraint solving. It answers: "If my primary trading strategy is requesting to operate at risk level **a**, but the current global market volatility cap dictates a maximum overall risk of **c**, what is the absolute highest risk level I can mathematically allow my sub-execution routines to utilize?"

### 4. How do I run the app?
No external dependencies are required. Run the application via the standard Python CLI. 

To see the help menu and system domain structure, run:
* `python app.py`

To execute the mathematical operations, use the following commands:
* `python app.py check <current_state> <target_limit>`
* `python app.py combine <state_a> <state_b>`
* `python app.py delegate <primary_strategy_state> <global_cap_state>`

### 5. What does a sample output look like?
```bash
$ python app.py delegate full_risk paper_trade

+------------------------------------------------------------------+
|               DYNAMIC FOREX RISK CONSTRAINT SYSTEM               |
+------------------------------------------------------------------+
 [ SYSTEM DOMAIN: THE RISK QUANTALE ]
   Hierarchy : halted < observe_only < paper_trade < micro_lot < full_risk
   Operation : ⊗ (Composition) -> Strict Meet (Strictest Rule Applies)
   Residual  : → (Delegation)  -> Backward Constraint Solver
+------------------------------------------------------------------+

 [ TASK: MAX DELEGATION CALCULATION (RESIDUAL →) ]
   Goal: If the primary strategy requests a specific risk level,
         but market conditions restrict the overall system cap,
         calculate the max risk allowed for sub-routines.

   > Primary Strategy Request : full_risk
   > Global Market Cap Limit  : paper_trade
   > Solving                  : full_risk → paper_trade

 [ RESULT ]
   ==================================================
   => MAX SAFE SUB-ROUTINE DELEGATION: [ PAPER_TRADE ]
   ==================================================
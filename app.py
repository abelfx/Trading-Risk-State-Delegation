import sys
from quantale_core import build_risk_quantale

def print_banner(q):
    """Prints a styled terminal header explaining the domain structure."""
    print("\n+" + "-"*66 + "+")
    print("|" + "DYNAMIC FOREX RISK CONSTRAINT SYSTEM".center(66) + "|")
    print("+" + "-"*66 + "+")
    print(" [ SYSTEM DOMAIN: THE RISK QUANTALE ]")
    print(f"   Hierarchy : {' < '.join(q.base)}")
    print("   Operation : ⊗ (Composition) -> Strict Meet (Strictest Rule Applies)")
    print("   Residual  : → (Delegation)  -> Backward Constraint Solver")
    print("+" + "-"*66 + "+\n")

def main():
    q = build_risk_quantale()
    args = sys.argv[1:]

    # If no arguments are passed, show a rich help menu
    if len(args) == 0:
        print_banner(q)
        print(" [ USAGE ]")
        print("   python app.py check <current_state> <target_limit>")
        print("     -> Verifies hierarchy (≤).")
        print("\n   python app.py combine <system_a> <system_b>")
        print("     -> Calculates effective composed risk (forward composition ⊗).")
        print("\n   python app.py delegate <primary_strategy> <global_cap>")
        print("     -> Calculates max safe sub-routine delegation (right residual →).\n")
        return

    command = args[0]

    # Handler for Order Verification (≤)
    if command == "check" and len(args) == 3:
        current_state = args[1]
        target_state = args[2]
        
        if current_state not in q.base or target_state not in q.base:
            print(f"\n[!] ERROR: Invalid state. Must be one of: {q.base}\n")
            return

        print_banner(q)
        print(" [ TASK: HIERARCHY CHECK (≤) ]")
        print("   Goal: Verify if a current state is safely within or equal to")
        print("         a target risk tier.\n")
        print(f"   > Current State  : {current_state}")
        print(f"   > Target Limit   : {target_state}")
        print(f"   > Solving        : {current_state} ≤ {target_state}\n")

        is_safe = q.can_do(current_state, target_state)

        print(" [ RESULT ]")
        print("   " + "="*50)
        if is_safe:
            print(f"   => STATUS: [ APPROVED ] {current_state} is within limits.")
        else:
            print(f"   => STATUS: [ DENIED ] {current_state} exceeds limits.")
        print("   " + "="*50 + "\n")

    # Handler for Forward Composition (⊗)
    elif command == "combine" and len(args) == 3:
        sys_a = args[1]
        sys_b = args[2]
        
        if sys_a not in q.base or sys_b not in q.base:
            print(f"\n[!] ERROR: Invalid state. Must be one of: {q.base}\n")
            return

        print_banner(q)
        print(" [ TASK: COMPOSITION CALCULATION (⊗) ]")
        print("   Goal: Calculate the effective risk posture when two active")
        print("         systems or algorithms interact.\n")
        print(f"   > System A State : {sys_a}")
        print(f"   > System B State : {sys_b}")
        print(f"   > Solving        : {sys_a} ⊗ {sys_b}\n")

        result = q.compose(sys_a, sys_b)

        print(" [ RESULT ]")
        print("   " + "="*50)
        print(f"   => EFFECTIVE COMPOSED RISK: [ {result.upper()} ]")
        print("   " + "="*50 + "\n")

    # Handler for the Right Residual (Delegation →)
    elif command == "delegate" and len(args) == 3:
        strat = args[1]
        cap = args[2]
        
        if strat not in q.base or cap not in q.base:
            print(f"\n[!] ERROR: Invalid state. Must be one of: {q.base}\n")
            return

        print_banner(q)
        print(" [ TASK: MAX DELEGATION CALCULATION (RESIDUAL →) ]")
        print("   Goal: If the primary strategy requests a specific risk level,")
        print("         but market conditions restrict the overall system cap,")
        print("         calculate the max risk allowed for sub-routines.\n")
        print(f"   > Primary Strategy Request : {strat}")
        print(f"   > Global Market Cap Limit  : {cap}")
        print(f"   > Solving                  : {strat} → {cap}\n")

        result = q.max_delegatable(strat, cap)

        print(" [ RESULT ]")
        print("   " + "="*50)
        print(f"   => MAX SAFE SUB-ROUTINE DELEGATION: [ {result.upper()} ]")
        print("   " + "="*50 + "\n")

    else:
        print("\n[!] ERROR: Invalid command or arguments.")
        print("    Run 'python app.py' to see usage.\n")

if __name__ == "__main__":
    main()
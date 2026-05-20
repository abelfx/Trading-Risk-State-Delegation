import sys
from quantale_core import build_risk_quantale

def main():
    q = build_risk_quantale()
    
    # Clean, minimalist CLI output
    print("\n=== Dynamic Forex Risk Constraint System ===")
    
    args = sys.argv[1:]
    
    if len(args) == 3 and args[0] == "delegate":
        primary_strat = args[1]
        global_cap = args[2]
        
        if primary_strat not in q.base or global_cap not in q.base:
            print(f"Error: Invalid states. Available states: {q.base}")
            return
            
        result = q.max_delegatable(primary_strat, global_cap)
        print(f"Primary Strategy:  {primary_strat}")
        print(f"Global Market Cap: {global_cap}")
        print(f"-> Max Sub-routine Delegation: {result}")
        
    elif len(args) == 3 and args[0] == "combine":
        state_a = args[1]
        state_b = args[2]
        
        if state_a not in q.base or state_b not in q.base:
            print(f"Error: Invalid states. Available states: {q.base}")
            return
            
        result = q.compose(state_a, state_b)
        print(f"System A: {state_a}")
        print(f"System B: {state_b}")
        print(f"-> Effective Composed Risk: {result}")
        
    else:
        print("Usage:")
        print("  python app.py combine <state1> <state2>")
        print("  python app.py delegate <primary_strategy_state> <global_cap_state>")
        print(f"\nValid states: {q.base}")

if __name__ == "__main__":
    main()

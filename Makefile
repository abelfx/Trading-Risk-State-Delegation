# ==========================================
# Dynamic Forex Risk Constraint System
# ==========================================

# Default states (can be overridden in the CLI)
STRAT ?= full_risk
CAP ?= paper_trade
STATE_A ?= observe_only
STATE_B ?= micro_lot

.PHONY: help check combine delegate demo

# Shows the standard help menu
help:
	@python3 app.py

# Runs the hierarchy check
check:
	@python3 app.py check $(STRAT) $(CAP)

# Runs the forward composition
combine:
	@python3 app.py combine $(STATE_A) $(STATE_B)

# Runs the backward constraint solver (Right Residual)
delegate:
	@python3 app.py delegate $(STRAT) $(CAP)

# Runs a full system demonstration for graders
demo:
	@echo "\n>>> RUNNING FULL SYSTEM DEMONSTRATION <<<\n"
	@python3 app.py check paper_trade full_risk
	@python3 app.py combine micro_lot paper_trade
	@python3 app.py delegate full_risk observe_only
	@echo "\n>>> DEMONSTRATION COMPLETE <<<\n"
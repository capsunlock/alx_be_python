match protective_action:
    case "wore a condom":
        return "not pregnant"
    case "pulled out":
        return "not pregnant"
    case "took the pill":
        return "not pregnant"
    case _: # "slept with another guy"
        return "pregnant"
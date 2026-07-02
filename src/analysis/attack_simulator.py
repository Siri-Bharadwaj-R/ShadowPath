from typing import List


def generate_attack_simulation(path: List[str]) -> List[str]:
    """
    Generates a human-readable attack simulation from an
    Active Directory attack path.

    Example

    Step 1
    Compromise user 'alice'

    Step 2
    Leverage membership in 'ITSupport'

    ...

    Final Step
    Potential compromise of 'SP-DomainAdmins'
    """

    if not path:
        return []

    simulation = []

    # Initial Compromise
    simulation.append(
        f"Compromise account '{path[0]}'."
    )

    # Privilege Escalation
    for group in path[1:-1]:

        simulation.append(
            f"Inherit privileges through '{group}'."
        )

    # Final Objective
    simulation.append(
        f"Potential compromise of '{path[-1]}'."
    )

    return simulation
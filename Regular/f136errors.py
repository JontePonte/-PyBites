
"""
Check red blood cell compatibility between donor and recipient.

For simplicity, only eight basic types of blood are considered.
The input of blood type can be in the form of:

Bloodtype enumeration
An integer value between 0 and 7
Textual representation e.g. "0-", "B+", "AB+", ...
There are 8 basic blood types based on presence or absence of three antigens: A, B, and Rh-D.

0- no antigens
0+ Rh-D antigen
A- antigen A
A+ antigen A and Rh-D
B- antigen B
B+ antigen B and Rh-D
AB- antigen A and B
AB+ all 3 antigens (A, B, Rh-D)


General rule:

An individual who does not have a certain antigen cannot receive a blood from someone who has that antigen.
Blood group 0 individuals do not have A or B antigens. Therefore, a group 0 individual can receive blood only from a group 0 individual, 
but can donate blood to individual with types A, B, 0 or AB.

Blood group A individuals have the A antigen.
Therefore, a group A individual can receive blood only from individuals of groups A or 0, 
and can donate blood to individuals with type A or AB.

Blood group B individuals have the B antigen. 
Therefore, a group B individual can receive blood only from individuals of groups B or 0, 
and can donate blood to individuals with type B or AB.

Blood group AB individuals have both A and B antigens. 
Therefore, an individual with type AB blood can receive blood from AB0, 
but cannot donate blood to any group other than AB.

Rh-D negative individuals do not have Rh-D antigen. 
Therefore, Rh-D negative can receive blood only from other Rh-D negative individuals.

Rh-D positive individuals have Rh-D antigen. 
Therefore, Rh-D positive individual can receive blood from both Rh-D negative or positive individuals.

Individuals with 0- are universal donors. Individuals with AB+ are universal recipients.

The rules described are general. 
In practice, there are over 340 different blood-group antigens.

Tasks Complete the function check_bt()
The function should check red blood cell compatibility between a donor and a recipient.

Return True for compatibility between the donor and the recipient, False otherwise.

If the input value is not a required type raise TypeError .
If the input value is not in the defined interval raise ValueError .



Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}

# complete :
def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """

    donor_int = convert_input_to_int(donor)
    recipient_int = convert_input_to_int(recipient)

    result_pac = _particular_antigen_comp(donor_int, recipient_int)
    
    # Resurn False if there is problem
    if -1 in result_pac:
        result = False
    else:
        result = True
    
    return result


def convert_input_to_int(input_val):
    # input is integer
    if type(input_val) == int:
        if input_val >= 0 and input_val <= 7:
            return input_val
        else:
            raise ValueError
    
    # input is Bloodtype
    elif type(input_val) == Bloodtype:
        return input_val.value

    # input is string
    elif type(input_val) == str:
        try:
            input_val = blood_type_text.get(input_val)
            return input_val.value
        except:
            raise ValueError
    
    # input is crazy
    else:
        raise TypeError



# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that 
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )

print(check_bt("0+",Bloodtype.A_NEG))
print(check_bt("0+","AB+"))
print(check_bt(7,"0+"))
print(check_bt(5,"häst"))


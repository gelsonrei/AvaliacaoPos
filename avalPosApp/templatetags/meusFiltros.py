from django import template
from material.admin.decorators import register

register = template.Library()

def in_reg(regs, reg):
    return regs.filter(id_registro=reg)

register.filter('in_reg', in_reg)
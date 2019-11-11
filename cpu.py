"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Add list properties to the `CPU` class to hold 256 bytes of memory

        # Add properties for internal registers

        self.reg = [0] * 8
        self.ram = [0] * 0xFF * 256
        self.PC = self.reg[0]
        self.SP = 0xF3
        self.asm_tbl = {}
        self.asm_table[0b00000001] = self.asm_hlt
        self.asm_table[0b10000010] = self.asm_ldi
        self.asm_table[0b01000111] = self.asm_prn
        self.asm_table[0b10100010] = self.asm_mul
        self.asm_table[0b01010000] = self.asm_add
        self.asm_table[0b01000101] = self.asm_push
        self.asm_table[0b01000110] = self.asm_pop
        self.asm_table[0b01010000] = self.asm_call
        self.asm_table[0b00010001] = self.asm_ret
        self.asm_table[0b10100111] = self.asm_cmp
        self.asm_table[0b01010100] = self.asm_jmp
        self.asm_table[0b01010101] = self.asm_jeq
        self.asm_table[0b01010110] = self.asm_jne

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value

    def asm_cmp(self, oper_a, oper_b):
        self.alu("MUL", oper_a, oper_b)
        self.PC += 3

    def asm_jmp(self):
    def asm_jeq(self):
    def asm_jne(self):

    def asm_hlt(self, oper_a, oper_b):
        return (0, False)

    def asm_ldi(self, oper_a, oper_b):
        oper_a = self.ram[self.PC + 1]
        oper_b = self.ram[self.PC + 2]
        self.reg[oper_a] = oper_b

    def asm_prn(self, oper_a):
        oper_a = self.ram[self.PC + 2]
        print(self.reg[oper_a])

    def asm_push(self, oper_a):
        self.SP = (self.SP - 1) % 255
        self.ram[self.SP] = self.reg[oper_a]

    def asm_pop(self, oper_a):
        value = self.ram[self.SP]
        self.reg[oper_a] = value
        self.SP + 1
        self.PC += 2

    def asm_call(self, oper_a):
        self.asm_push(oper_a)
        self.ram[self.SP] = self.PC + 2
        self.PC = self.reg[oper_a]

    def asm_ret(self):
        self.PC = self.ram[self.SP]

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        """ program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ] """

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] = (self.reg[reg_a] * self.reg[reg_b])
        elif op == "CMP":
            if self.reg[reg_a] > self.reg[reg_b]:
                self.flag = 0b00000010
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.flag = 0b00000100
            elif self.reg[reg_a] == self.reg[reg_b]:
                self.flag = 0b00000001
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        IR = self.ram[self.PC]


import random
#Cocotb libs
import cocotb
from cocotb.triggers import Timer, RisingEdge


class Connection:
    def __init__(self, dut):
        self.dut = dut
        # Init interface
        self.apb = ApbMaster(dut.apb, name=None, clock=dut.clk)

@cocotb.test()
async def simple_test(dut):
    ### Create connection ###
    connect_with_dut = Connection(dut)  # Connect with DUT phase
    ###   Start   reset   ###
    await reset_on_clock(dut.rstn, dut.clk, active_level=0)
    ### Set length for random data in bytes ###
    length = 4
    ### Random data with "length" size in byte ###
    test_data = int.from_bytes(random.randbytes(length), byteorder='little')
    test_addr = 0x0
    ### Send APB word ###
    await connect_with_dut.apb.write(test_addr, test_data)
    ### Read APB word ###
    data_from_apb = await connect_with_dut.apb.read(test_addr)
    ### Comaparing 2 frames ###
    assert test_data == data_from_apb, f"Incorrect, please check your input and output APB word"
    ### Wait 100 ns ###
    await Timer(100, 'ns') # Wait 100 ns


@cocotb.coroutine # Func for reset
async def reset_on_clock(reset_signal, clock, active_level:int=0, click_time:int=10):
    """ The function clamps 'reset_signal' for a certain number of clock cycles (click_time)."""
    if active_level == 1:
        init_value=0
    else:
        init_value=1
    reset_signal.value = active_level
    for _ in range(click_time):
        await RisingEdge(clock)
    reset_signal.value = init_value

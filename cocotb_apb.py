import cocotb
import logging
from cocotb.triggers import RisingEdge
from cocotb_bus.drivers import BusDriver

class ApbMaster(BusDriver):

    _signals = ["psel","pwrite", "strb", "pwdata", "paddr",
            "penable", "pready", "prdata"]
    def __init__(self, entity, name, clock):
        super().__init__(self, entity, name, clock)

        self.bus.psel.setimmediatevalue(0)
        self.bus.pwrite.setimmediatevalue(0)
        self.bus.pstrb.setimmediatevalue(0)
        self.bus.pwdata.setimmediatevalue(0)
        self.bus.paddr.setimmediatevalue(0)

    async def write(self,addr,data,strb=0xF,verbose=False):
        await RisingEdge(self.clock)

        self.bus.psel.value = 1
        self.bus.penable.value = 0
        self.bus.pwrite.value = 1
        self.bus.pwdata.value = data
        self.bus.paddr.value = addr
        self.bus.pstrb.value = strb

        await RisingEdge(self.clock)
        self.bus.penable.value = 1
        while True:
            await RisingEdge(self.clock)
            if self.bus.penable.value and self.bus.pready.value:
                break

        self.bus.psel.value = 0
        self.bus.penable.value = 0
        self.bus.pwrite.value = 0
        self.bus.pwdata.value = 0
        self.bus.paddr.value = 0
        self.bus.pstrb.value = 0

        if verbose:
            logging.critical(f"Address = {hex(addr)},  data  = {hex(data)}")

    async def read(self,addr,verbose=False):
        await RisingEdge(self.clock)

        self.bus.psel.value = 1
        self.bus.penable.value = 0
        self.bus.pwrite.value = 0
        self.bus.pwdata.value = 0
        self.bus.paddr.value = addr
        self.bus.pstrb.value = 0

        await RisingEdge(self.clock)
        self.bus.penable.value = 1

        while True:
            await RisingEdge(self.clock)
            if self.bus.penable.value and self.bus.pready.value:
                break

        tmp = self.bus.prdata.value

        if verbose:
            logging.critical(f"Address = {hex(addr)},  data  = {hex(data)}")

        self.bus.psel.value = 0
        self.bus.penable.value = 0
        self.bus.pwrite.value = 0
        self.bus.pwdata.value = 0
        self.bus.paddr.value = 0
        self.bus.pstrb.value = 0

        return tmp.integer

# class ApbSlave(BusDriver):

#     _signals = ["pready","prdata","penable","psel"]

#     def __init__(self, entity, name, clock, size=4, offset=0, **kwargs):

#         BusDriver.__init__(self,entity,name,clock,**kwargs)
#         self.bus.pready.setimmediatevalue(1)
#         self.bus.prdata.setimmediatevalue(0)

#         self.memory = np.zeros(size//4, dtype=int)
#         self.offset = offset

#         cocotb.fork(self.wait())

#     async def wait(self):
#         while True:
#             await FallingEdge(self.clock)
#             await ReadOnly()
#             if self.bus.penable.value and self.bus.psel.value and self.bus.s.pready.value:
                
#                 addr = (int(self.bus.paddr) - self.offset)//4
#                 data = int(self.bus.pwdata)
#                 if (self.bus.pwrite.value):
#                     self.write(addr,data)
#                 else:
#                     await self.read(addr)
        
#     def write(self,addr,data):
#         self.log.info("Memory write: %x %x",addr,data)
#         self.memory[addr] = data

#     async def read(self,addr):
#         self.log.info("Memory read: %x %x",addr,self.memory[addr])
#         await NextTimeStep()
#         self.bus.prdata <= int(self.memory[addr])
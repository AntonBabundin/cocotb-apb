
import generate_filelist_for_questa as questa
from cocotb_test.simulator import run
import os

_gui_start  = bool(int(os.environ["GUI"]))
settings = questa.get_questa_settings(coverage=False, xcelium=True)

sim_args = []

_test_name = "apb_template_seq"

if (os.environ['WAVES'] == "1"):
    sim_args.append('-input {:}/scripts/tcl/xcelium_database.tcl'.format(os.environ['PROJECT_HOME']))

def test_axi_template():
    run(
        vhdl_sources         = settings['vhdl_sources'],                                     # vhdl sources
        verilog_sources      = settings['verilog_sources'],                                  # verilog sources
        includes             = settings['includes'],
        python_search        = settings['python_search'],                                    # python directories
        
        extra_args           = settings['extra_args'],
        sim_args             = sim_args,
        sim_build            = settings['sim_build'],

        force_compile        = True,
        toplevel_lang        = 'verilog',
        gui                  = _gui_start,
        toplevel             = "{:}.{:}".format(settings['work_lib'],settings['toplevel']),  # top level HDL
        module               = _test_name                                                    # name of cocotb test module
    )

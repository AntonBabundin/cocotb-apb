export MODULE_HOME = $(shell git rev-parse --show-toplevel)
export PROJECT_HOME = $(MODULE_HOME)/../../
export MODULES_DIR = $(PROJECT_HOME)/src
export TOPLEVEL = tb
export FILELIST = all.yaml
export TOOL = xcelium
export WORK_LIB = artec3d
export LOG_SIM = True
include $(PROJECT_HOME)/scripts/make/xcelium.make

export PYTHON_TEST_FILE = $(PWD)/apb_template_test.py

echo:
	echo $(PROJECT_HOME)
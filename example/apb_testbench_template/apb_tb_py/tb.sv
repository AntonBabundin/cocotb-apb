`timescale  1 ps / 1 ps

module tb;

    logic clk;
    logic rstn;

    artec_apb_if apb();

// ******************************************************* //
// Clocks
// ******************************************************* //
    initial begin
        clk = 1'b0;
        forever begin
            #(1);
            clk = ~clk;
        end
    end

// ******************************************************* //
// DUT 
// ******************************************************* //
    apb_source_template i_dut (
        .clk         (clk  ),
        .rstn        (rstn ),
        .apb         (apb)
    );
endmodule
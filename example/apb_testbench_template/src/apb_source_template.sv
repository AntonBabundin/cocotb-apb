`timescale 1ps / 1ps


module apb_source_template (
    input                            clk       ,
    input                            rstn      ,
    artec_apb_if.slave               apb       
    );

    assign apb.pready = 1'b1;
    logic write;
    reg [31:0] register;
    assign apb.prdata = (apb.psel) ? (
                                     (apb.paddr[7:2] ==  0)  ? {register} : 32'b0
                                     ) : 32'b0;
    // ******************************************************* //
    // Write 
    // ******************************************************* //
    assign write = apb.psel & apb.penable & apb.pwrite;
    // ******************************************************* //
    // Register 
    // ******************************************************* //
    always_ff @(posedge clk or negedge rstn) begin : proc_register
        if(~rstn) begin
            register <= 0;
        end else begin
            register <= write && apb.paddr[7:2]==0 ? apb.pwdata : register;
        end
    end
endmodule

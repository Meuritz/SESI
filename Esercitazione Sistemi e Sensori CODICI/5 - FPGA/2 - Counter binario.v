module counter_binario(
    input clk,
    output reg[15:0] LED
);

    reg [64:0] counter;
    initial begin
        counter = 0;
    end

    always @(posedge clk) begin
        counter <= counter + 1;

        for (integer i = 0; i < 16; i = i + 1) begin
            LED[i] <= counter[19 + i];
        end
    end
endmodule

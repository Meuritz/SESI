========================================
//led lampeggio
========================================
module led_lampeggio(
    input clk,
    output reg[7:0] LED
);

    reg [32:0] counter;
    initial 
        counter = 0;

    always @(posedge clk) begin
        LED[0] <= counter[25];
        counter <= counter + 1;
    end
endmodule

========================================
//led lampeggio con switch
========================================

module led_lampeggio_on(
    input clk,
    input sw[7:0],
    output reg[7:0] LED
);

    reg [32:0] counter;
    initial 
        counter = 0;

    always @(posedge clk) begin
        if (sw[0] == 1) begin
            LED[0] <= counter[25];
            counter <= counter + 1;
        end
        if (sw[0] == 0) begin
            LED[0] <= 0;
        end
    end
endmodule

========================================
//led lampeggio con frequenza doppia con switch off
========================================

module led_lampeggio_on_off(
    input clk,
    input sw[7:0],
    output reg[7:0] LED
);

    reg [32:0] counter;
    initial 
        counter = 0;

    always @(posedge clk) begin
        if (sw[0] == 1) begin
            LED[0] <= counter[25];
            counter <= counter + 1;
        end
        if (sw[0] == 0) begin
            LED[0] <= counter[24];
            counter <= counter + 1;
        end
    end
endmodule

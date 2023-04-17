#!/usr/bin/perl
use strict;
use warnings;

#using bignum
my @ A3 = (1,2,3,4,5,6,7,8);
my @ B3 = (8,7,6,5,4,3,2,1);
# (-104, 14, 12, 10, 152, 42, 4, 74)

my @ A = (0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0);
my @ B = (0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0);
# 000000000000000


print " DIMMENSION \n";
print scalar(@A);
print " DIMMENSION \n";
print scalar(@B);

my @cay1 = cayley(\@A, \@B);
print "Hello World \n";
print "hello." . "\n";

print join(", ", @cay1);


sub cayley {
    my ($ref1, $ref2) = @_;
    my @input1 = @{$ref1};
    my @input2 = @{$ref2};
    #print join(", ", @input1);
    #print " \n";
    #print join(", ", @input2);
    my $order1 = scalar(@input1);
    my $order2 = scalar(@input2);
    my @output;
    if ($order1 != $order2) {
        die;
    }
    if ($order1 == 1) {
        $output[0] = $input1[0]*$input2[0];
    } else {
        my @A       = @input1[ 0 .. $order1 / 2 - 1 ];
        my @B       = @input1[ $order1 / 2 .. $order1 - 1 ];
        my @C       = @input2[ 0 .. $order1 / 2 - 1 ];
        my @D       = @input2[ $order1 / 2 .. $order1 - 1 ];
        my $lengthZ = scalar(@D);
        my @conjD;
        my @conjC;
        my $indexZ;

        for $indexZ (0 .. $lengthZ - 1) {
            if ($indexZ == 0) {
                $conjC[$indexZ] = $C[$indexZ];
                $conjD[$indexZ] = $D[$indexZ];
            } else {
                $conjC[$indexZ] = -$C[$indexZ];
                $conjD[$indexZ] = - $D[$indexZ];
            }
        }
        my @cay1 = cayley(\@A,     \@C);
        my @cay2 = cayley(\@conjD, \@B);
        my @cay3 = cayley(\@D,     \@A);
        my @cay4 = cayley(\@B,     \@conjC);
        my @left;
        my @right;
        my $length = scalar(@cay1);
        my $index;

        for $index (0 .. $length - 1) {
            $left[$index]  = $cay1[$index] -  $cay2[$index];
            $right[$index] = $cay3[$index] + $cay4[$index];
        }
        @output = (@left, @right);
    }
    return @output;
}
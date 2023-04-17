#!/usr/bin/perl
use strict;
use warnings;

#using bignum
my $Tindex = 0;
my @As     = (rand(), rand(), rand(), rand());
my @Cs     = (rand(), rand(), rand(), rand());

my @AZ = (
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand(),
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()
);
my @CZ = (
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand(),
    rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()
);

my @ADD = ('Ag0', 'Ag1', 'Ag2', 'Ag3', 'Ae4', 'Ae5', 'Ae6', 'Ae7');
my @BDD = ('G0',  'G1',  'G2',  'G3',  'E4',  'E5',  'E6',  'E7');

my @AX = ('Ag0', 'Ag1', 'Ag2', 'Ag3');
my @BX = ('G0',  'G1',  'G2',  'G3');

my @A = ('A', 'B', 'C', 'D');
my @B = ('E', 'F', 'G', 'H');



print " DIMMENSION \n";
print scalar(@A);
print " DIMMENSION \n";
print scalar(@B);

my @cay1 = cayley(\@A, \@B);
print "Hello World \n";
print "hello." . "\n";

print join(", ", @cay1);
print "\n" . $Tindex;

# my @C = ('C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7');
# my @cay2 = cayley(\@C, \@cay1);
# print "Hello World \n";
# print "hello." . "\n";
# print join(", ", @cay2);
# print "\n".$Tindex;

my $length = scalar(@cay1);
my $index;
my $str;
my @spl;
my @spl1;
my $find;
my $replace;
for $index (0 .. $length - 1) {
    print "$index \n";
    $str = $cay1[$index];

    # Here character is comma(, )
    # using split() function
    @spl = split(/[+-]/, $str);

    # displaying result using foreach loop
    my $strx = "";
    my $stry = "";
    my $strz = "";
    foreach my $i (@spl) {
        @spl1 = split(/[*]/, $i);
        $strz    = join("*", sort(@spl1));
        $find    = "m";
        $replace = "-";
        $strz =~ s/$find/$replace/;
        $find    = "p";
        $replace = "+";
        $strz =~ s/$find/$replace/;
        $strx = $strx . $strz;
    }
    print("", $strx);
    print "\n";
}

# my $length = scalar(@cay2);
# my $index;
# my $str;
# my @spl;
# for $index (0 .. $length - 1) {
#     print "$index \n";
# $str  = $cay2[$index];
# # Here character is comma(, )
# # using split() function
# @spl = split(/[+-]/, $str);
# # displaying result using foreach loop
# foreach my $i (@spl)
# {
#     print "$i \n";
# }
# }

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
        $output[0] = $input1[0] . "*" . $input2[0];
    } else {
        $Tindex = $Tindex + 1;
        my @Aaa  = @input1[ 0 .. $order1 / 2 - 1 ];
        my @Baa  = @input1[ $order1 / 2 .. $order1 - 1 ];
        my @Caa  = @input2[ 0 .. $order1 / 2 - 1 ];
        my @Daa  = @input2[ $order1 / 2 .. $order1 - 1 ];
        my @cay1 = cayley(\@Aaa, \@Caa);
        my @cay2 = cayley(conj(\@Daa), \@Baa);
        my @cay3 = cayley(\@Daa, \@Aaa);
        my @cay4 = cayley(\@Baa, conj(\@Caa));
        my @left;
        my @right;
        my $length = scalar(@cay1);
        my $index;

        for $index (0 .. $length - 1) {
            $left[$index]  = $cay1[$index] . '-m-' . $cay2[$index];
            $right[$index] = $cay4[$index] . '+p+' . $cay3[$index];
        }
        @output = (@left, @right);
    }
    return @output;
}

sub conj {
    my @input1A = @_;
    my $order1A = scalar(@input1A);
    my @outputA;
    if ($order1A == 1) {
        $outputA[0] = $input1A[0];
    } else {
        my @AA      = @input1A[ 0 .. $order1A / 2 - 1 ];
        my @BA      = @input1A[ $order1A / 2 .. $order1A - 1 ];
        my @BAe;
        my $lengthA = scalar(@BA);
        my $indexA;
        for $indexA (0 .. $lengthA - 1) {
            $BAe[$indexA] = '-m-' . $BA[$indexA];
        }
        @outputA = (conj(\@AA), @BAe);
    }
    return @outputA;
}
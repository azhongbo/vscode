#!/usr/bin/python3
import os,sys

if os.name == 'posix':
    home_folder = os.environ['HOME']
    os.system(f"mkdir -p {home_folder}/.vscode/extensions/ryanCode/out")

if os.name == 'nt':
    home_folder = os.environ['USERPROFILE']
    os.system(f"mkdir {home_folder}\\.vscode\\extensions\\ryanCode\\out")


def saveDefault(filename,text):
    savefile = ""

    if os.name == 'posix':
        home_folder = os.environ['HOME']
        savefile   = f'{home_folder}/.vscode/extensions/ryanCode/{filename}'        

    if os.name == 'nt':
        home_folder = os.environ['USERPROFILE']
        savefile   = f'{home_folder}\\.vscode\\extensions\\ryanCode\\{filename}'

    # savefile = '/home/ubuntu-mate/.vscode/extensions/ryanCode/' + filename
    fp = open( savefile ,'w')
    fp.write(text)
    fp.close


filename = 'README.md'
text = '''# helloworld README
Hello World
'''
saveDefault(filename,text)


filename = 'CHANGELOG.md'
text = '''
# Change Log
'''
saveDefault(filename,text)


filename = 'package-lock.json'
text = '''{
    "name": "helloworld",
    "version": "1.0.8",
    "lockfileVersion": 1,
    "requires": true,
    "dependencies": {
        "@types/mocha": {
            "version": "2.2.48",
            "resolved": "https://registry.npmjs.org/@types/mocha/-/mocha-2.2.48.tgz",
            "integrity": "sha512-nlK/iyETgafGli8Zh9zJVCTicvU3iajSkRwOh3Hhiva598CMqNJ4NcVCGMTGKpGpTYj/9R8RLzS9NAykSSCqGw==",
            "dev": true
        },
        "@types/node": {
            "version": "8.10.29",
            "resolved": "https://registry.npmjs.org/@types/node/-/node-8.10.29.tgz",
            "integrity": "sha512-zbteaWZ2mdduacm0byELwtRyhYE40aK+pAanQk415gr1eRuu67x7QGOLmn8jz5zI8LDK7d0WI/oT6r5Trz4rzQ==",
            "dev": true
        },
        "ajv": {
            "version": "5.5.2",
            "resolved": "https://registry.npmjs.org/ajv/-/ajv-5.5.2.tgz",
            "integrity": "sha1-c7Xuyj+rZT49P5Qis0GtQiBdyWU=",
            "dev": true,
            "requires": {
                "co": "4.6.0",
                "fast-deep-equal": "1.1.0",
                "fast-json-stable-stringify": "2.0.0",
                "json-schema-traverse": "0.3.1"
            }
        },
        "ansi-cyan": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/ansi-cyan/-/ansi-cyan-0.1.1.tgz",
            "integrity": "sha1-U4rlKK+JgvKK4w2G8vF0VtJgmHM=",
            "dev": true,
            "requires": {
                "ansi-wrap": "0.1.0"
            }
        },
        "ansi-red": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/ansi-red/-/ansi-red-0.1.1.tgz",
            "integrity": "sha1-jGOPnRCAgAo1PJwoyKgcpHBdlGw=",
            "dev": true,
            "requires": {
                "ansi-wrap": "0.1.0"
            }
        },
        "ansi-regex": {
            "version": "2.1.1",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
            "integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8=",
            "dev": true
        },
        "ansi-styles": {
            "version": "2.2.1",
            "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz",
            "integrity": "sha1-tDLdM1i2NM914eRmQ2gkBTPB3b4=",
            "dev": true
        },
        "ansi-wrap": {
            "version": "0.1.0",
            "resolved": "https://registry.npmjs.org/ansi-wrap/-/ansi-wrap-0.1.0.tgz",
            "integrity": "sha1-qCJQ3bABXponyoLoLqYDu/pF768=",
            "dev": true
        },
        "argparse": {
            "version": "1.0.10",
            "resolved": "https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz",
            "integrity": "sha512-o5Roy6tNG4SL/FOkCAN6RzjiakZS25RLYFrcMttJqbdd8BWrnA+fGz57iN5Pb06pvBGvl5gQ0B48dJlslXvoTg==",
            "dev": true,
            "requires": {
                "sprintf-js": "1.0.3"
            }
        },
        "arr-diff": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/arr-diff/-/arr-diff-1.1.0.tgz",
            "integrity": "sha1-aHwydYFjWI/vfeezb6vklesaOZo=",
            "dev": true,
            "requires": {
                "arr-flatten": "1.1.0",
                "array-slice": "0.2.3"
            }
        },
        "arr-flatten": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz",
            "integrity": "sha512-L3hKV5R/p5o81R7O02IGnwpDmkp6E982XhtbuwSe3O4qOtMMMtodicASA1Cny2U+aCXcNpml+m4dPsvsJ3jatg==",
            "dev": true
        },
        "arr-union": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/arr-union/-/arr-union-2.1.0.tgz",
            "integrity": "sha1-IPnqtexw9cfSFbEHexw5Fh0pLH0=",
            "dev": true
        },
        "array-differ": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/array-differ/-/array-differ-1.0.0.tgz",
            "integrity": "sha1-7/UuN1gknTO+QCuLuOVkuytdQDE=",
            "dev": true
        },
        "array-slice": {
            "version": "0.2.3",
            "resolved": "https://registry.npmjs.org/array-slice/-/array-slice-0.2.3.tgz",
            "integrity": "sha1-3Tz7gO15c6dRF82sabC5nshhhvU=",
            "dev": true
        },
        "array-union": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/array-union/-/array-union-1.0.2.tgz",
            "integrity": "sha1-mjRBDk9OPaI96jdb5b5w8kd47Dk=",
            "dev": true,
            "requires": {
                "array-uniq": "1.0.3"
            }
        },
        "array-uniq": {
            "version": "1.0.3",
            "resolved": "https://registry.npmjs.org/array-uniq/-/array-uniq-1.0.3.tgz",
            "integrity": "sha1-r2rId6Jcx/dOBYiUdThY39sk/bY=",
            "dev": true
        },
        "array-unique": {
            "version": "0.2.1",
            "resolved": "https://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz",
            "integrity": "sha1-odl8yvy8JiXMcPrc6zalDFiwGlM=",
            "dev": true
        },
        "arrify": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz",
            "integrity": "sha1-iYUI2iIm84DfkEcoRWhJwVAaSw0=",
            "dev": true
        },
        "asn1": {
            "version": "0.2.4",
            "resolved": "https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz",
            "integrity": "sha512-jxwzQpLQjSmWXgwaCZE9Nz+glAG01yF1QnWgbhGwHI5A6FRIEY6IVqtHhIepHqI7/kyEyQEagBC5mBEFlIYvdg==",
            "dev": true,
            "requires": {
                "safer-buffer": "2.1.2"
            }
        },
        "assert-plus": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
            "integrity": "sha1-8S4PPF13sLHN2RRpQuTpbB5N1SU=",
            "dev": true
        },
        "asynckit": {
            "version": "0.4.0",
            "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
            "integrity": "sha1-x57Zf380y48robyXkLzDZkdLS3k=",
            "dev": true
        },
        "aws-sign2": {
            "version": "0.7.0",
            "resolved": "https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz",
            "integrity": "sha1-tG6JCTSpWR8tL2+G1+ap8bP+dqg=",
            "dev": true
        },
        "aws4": {
            "version": "1.8.0",
            "resolved": "https://registry.npmjs.org/aws4/-/aws4-1.8.0.tgz",
            "integrity": "sha512-ReZxvNHIOv88FlT7rxcXIIC0fPt4KZqZbOlivyWtXLt8ESx84zd3kMC6iK5jVeS2qt+g7ftS7ye4fi06X5rtRQ==",
            "dev": true
        },
        "babel-code-frame": {
            "version": "6.26.0",
            "resolved": "https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz",
            "integrity": "sha1-Y/1D99weO7fONZR9uP42mj9Yx0s=",
            "dev": true,
            "requires": {
                "chalk": "1.1.3",
                "esutils": "2.0.2",
                "js-tokens": "3.0.2"
            },
            "dependencies": {
                "chalk": {
                    "version": "1.1.3",
                    "resolved": "http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz",
                    "integrity": "sha1-qBFcVeSnAv5NFQq9OHKCKn4J/Jg=",
                    "dev": true,
                    "requires": {
                        "ansi-styles": "2.2.1",
                        "escape-string-regexp": "1.0.5",
                        "has-ansi": "2.0.0",
                        "strip-ansi": "3.0.1",
                        "supports-color": "2.0.0"
                    }
                }
            }
        },
        "balanced-match": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz",
            "integrity": "sha1-ibTRmasr7kneFk6gK4nORi1xt2c=",
            "dev": true
        },
        "bcrypt-pbkdf": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz",
            "integrity": "sha1-pDAdOJtqQ/m2f/PKEaP2Y342Dp4=",
            "dev": true,
            "optional": true,
            "requires": {
                "tweetnacl": "0.14.5"
            }
        },
        "block-stream": {
            "version": "0.0.9",
            "resolved": "https://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz",
            "integrity": "sha1-E+v+d4oDIFz+A3UUgeu0szAMEmo=",
            "dev": true,
            "requires": {
                "inherits": "2.0.3"
            }
        },
        "brace-expansion": {
            "version": "1.1.11",
            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
            "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
            "dev": true,
            "requires": {
                "balanced-match": "1.0.0",
                "concat-map": "0.0.1"
            }
        },
        "braces": {
            "version": "1.8.5",
            "resolved": "https://registry.npmjs.org/braces/-/braces-1.8.5.tgz",
            "integrity": "sha1-uneWLhLf+WnWt2cR6RS3N4V79qc=",
            "dev": true,
            "requires": {
                "expand-range": "1.8.2",
                "preserve": "0.2.0",
                "repeat-element": "1.1.3"
            }
        },
        "browser-stdout": {
            "version": "1.3.0",
            "resolved": "https://registry.npmjs.org/browser-stdout/-/browser-stdout-1.3.0.tgz",
            "integrity": "sha1-81HTKWnTL6XXpVZxVCY9korjvR8=",
            "dev": true
        },
        "buffer-crc32": {
            "version": "0.2.13",
            "resolved": "https://registry.npmjs.org/buffer-crc32/-/buffer-crc32-0.2.13.tgz",
            "integrity": "sha1-DTM+PwDqxQqhRUq9MO+MKl2ackI=",
            "dev": true
        },
        "buffer-from": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz",
            "integrity": "sha512-MQcXEUbCKtEo7bhqEs6560Hyd4XaovZlO/k9V3hjVUF/zwW7KBVdSK4gIt/bzwS9MbR5qob+F5jusZsb0YQK2A==",
            "dev": true
        },
        "builtin-modules": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/builtin-modules/-/builtin-modules-1.1.1.tgz",
            "integrity": "sha1-Jw8HbFpywC9bZaR9+Uxf46J4iS8=",
            "dev": true
        },
        "caseless": {
            "version": "0.12.0",
            "resolved": "https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz",
            "integrity": "sha1-G2gcIf+EAzyCZUMJBolCDRhxUdw=",
            "dev": true
        },
        "chalk": {
            "version": "2.4.1",
            "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.4.1.tgz",
            "integrity": "sha512-ObN6h1v2fTJSmUXoS3nMQ92LbDK9be4TV+6G+omQlGJFdcUX5heKi1LZ1YnRMIgwTLEj3E24bT6tYni50rlCfQ==",
            "dev": true,
            "requires": {
                "ansi-styles": "3.2.1",
                "escape-string-regexp": "1.0.5",
                "supports-color": "5.5.0"
            },
            "dependencies": {
                "ansi-styles": {
                    "version": "3.2.1",
                    "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz",
                    "integrity": "sha512-VT0ZI6kZRdTh8YyJw3SMbYm/u+NqfsAxEpWO0Pf9sq8/e94WxxOpPKx9FR1FlyCtOVDNOQ+8ntlqFxiRc+r5qA==",
                    "dev": true,
                    "requires": {
                        "color-convert": "1.9.3"
                    }
                },
                "supports-color": {
                    "version": "5.5.0",
                    "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz",
                    "integrity": "sha512-QjVjwdXIt408MIiAqCX4oUKsgU2EqAGzs2Ppkm4aQYbjm+ZEWEcW4SfFNTr4uMNZma0ey4f5lgLrkB0aX0QMow==",
                    "dev": true,
                    "requires": {
                        "has-flag": "3.0.0"
                    }
                }
            }
        },
        "clone": {
            "version": "0.2.0",
            "resolved": "https://registry.npmjs.org/clone/-/clone-0.2.0.tgz",
            "integrity": "sha1-xhJqkK1Pctv1rNskPMN3JP6T/B8=",
            "dev": true
        },
        "clone-buffer": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/clone-buffer/-/clone-buffer-1.0.0.tgz",
            "integrity": "sha1-4+JbIHrE5wGvch4staFnksrD3Fg=",
            "dev": true
        },
        "clone-stats": {
            "version": "0.0.1",
            "resolved": "https://registry.npmjs.org/clone-stats/-/clone-stats-0.0.1.tgz",
            "integrity": "sha1-uI+UqCzzi4eR1YBG6kAprYjKmdE=",
            "dev": true
        },
        "cloneable-readable": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/cloneable-readable/-/cloneable-readable-1.1.2.tgz",
            "integrity": "sha512-Bq6+4t+lbM8vhTs/Bef5c5AdEMtapp/iFb6+s4/Hh9MVTt8OLKH7ZOOZSCT+Ys7hsHvqv0GuMPJ1lnQJVHvxpg==",
            "dev": true,
            "requires": {
                "inherits": "2.0.3",
                "process-nextick-args": "2.0.0",
                "readable-stream": "2.3.6"
            }
        },
        "co": {
            "version": "4.6.0",
            "resolved": "https://registry.npmjs.org/co/-/co-4.6.0.tgz",
            "integrity": "sha1-bqa989hTrlTMuOR7+gvz+QMfsYQ=",
            "dev": true
        },
        "color-convert": {
            "version": "1.9.3",
            "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz",
            "integrity": "sha512-QfAUtd+vFdAtFQcC8CCyYt1fYWxSqAiK2cSD6zDB8N3cpsEBAvRxp9zOGg6G/SHHJYAT88/az/IuDGALsNVbGg==",
            "dev": true,
            "requires": {
                "color-name": "1.1.3"
            }
        },
        "color-name": {
            "version": "1.1.3",
            "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz",
            "integrity": "sha1-p9BVi9icQveV3UIyj3QIMcpTvCU=",
            "dev": true
        },
        "combined-stream": {
            "version": "1.0.6",
            "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.6.tgz",
            "integrity": "sha1-cj599ugBrFYTETp+RFqbactjKBg=",
            "dev": true,
            "requires": {
                "delayed-stream": "1.0.0"
            }
        },
        "commander": {
            "version": "2.18.0",
            "resolved": "https://registry.npmjs.org/commander/-/commander-2.18.0.tgz",
            "integrity": "sha512-6CYPa+JP2ftfRU2qkDK+UTVeQYosOg/2GbcjIcKPHfinyOLPVGXu/ovN86RP49Re5ndJK1N0kuiidFFuepc4ZQ==",
            "dev": true
        },
        "concat-map": {
            "version": "0.0.1",
            "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
            "integrity": "sha1-2Klr13/Wjfd5OnMDajug1UBdR3s=",
            "dev": true
        },
        "convert-source-map": {
            "version": "1.5.1",
            "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.5.1.tgz",
            "integrity": "sha1-uCeAl7m8IpNl3lxiz1/K7YtVmeU=",
            "dev": true
        },
        "core-util-is": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz",
            "integrity": "sha1-tf1UIgqivFq1eqtxQMlAdUUDwac=",
            "dev": true
        },
        "dashdash": {
            "version": "1.14.1",
            "resolved": "https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz",
            "integrity": "sha1-hTz6D3y+L+1d4gMmuN1YEDX24vA=",
            "dev": true,
            "requires": {
                "assert-plus": "1.0.0"
            }
        },
        "debug": {
            "version": "3.1.0",
            "resolved": "https://registry.npmjs.org/debug/-/debug-3.1.0.tgz",
            "integrity": "sha512-OX8XqP7/1a9cqkxYw2yXss15f26NKWBpDXQd0/uK/KPqdQhxbPa994hnzjcE2VqQpDslf55723cKPUOGSmMY3g==",
            "dev": true,
            "requires": {
                "ms": "2.0.0"
            }
        },
        "deep-assign": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/deep-assign/-/deep-assign-1.0.0.tgz",
            "integrity": "sha1-sJJ0O+hCfcYh6gBnzex+cN0Z83s=",
            "dev": true,
            "requires": {
                "is-obj": "1.0.1"
            }
        },
        "delayed-stream": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
            "integrity": "sha1-3zrhmayt+31ECqrgsp4icrJOxhk=",
            "dev": true
        },
        "diff": {
            "version": "3.5.0",
            "resolved": "https://registry.npmjs.org/diff/-/diff-3.5.0.tgz",
            "integrity": "sha512-A46qtFgd+g7pDZinpnwiRJtxbC1hpgf0uzP3iG89scHk0AUC7A1TGxf5OiiOUv/JMZR8GOt8hL900hV0bOy5xA==",
            "dev": true
        },
        "duplexer": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/duplexer/-/duplexer-0.1.1.tgz",
            "integrity": "sha1-rOb/gIwc5mtX0ev5eXessCM0z8E=",
            "dev": true
        },
        "duplexify": {
            "version": "3.6.0",
            "resolved": "https://registry.npmjs.org/duplexify/-/duplexify-3.6.0.tgz",
            "integrity": "sha512-fO3Di4tBKJpYTFHAxTU00BcfWMY9w24r/x21a6rZRbsD/ToUgGxsMbiGRmB7uVAXeGKXD9MwiLZa5E97EVgIRQ==",
            "dev": true,
            "requires": {
                "end-of-stream": "1.4.1",
                "inherits": "2.0.3",
                "readable-stream": "2.3.6",
                "stream-shift": "1.0.0"
            }
        },
        "ecc-jsbn": {
            "version": "0.1.2",
            "resolved": "https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz",
            "integrity": "sha1-OoOpBOVDUyh4dMVkt1SThoSamMk=",
            "dev": true,
            "optional": true,
            "requires": {
                "jsbn": "0.1.1",
                "safer-buffer": "2.1.2"
            }
        },
        "end-of-stream": {
            "version": "1.4.1",
            "resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.1.tgz",
            "integrity": "sha512-1MkrZNvWTKCaigbn+W15elq2BB/L22nqrSY5DKlo3X6+vclJm8Bb5djXJBmEX6fS3+zCh/F4VBK5Z2KxJt4s2Q==",
            "dev": true,
            "requires": {
                "once": "1.4.0"
            }
        },
        "escape-string-regexp": {
            "version": "1.0.5",
            "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz",
            "integrity": "sha1-G2HAViGQqN/2rjuyzwIAyhMLhtQ=",
            "dev": true
        },
        "esprima": {
            "version": "4.0.1",
            "resolved": "https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz",
            "integrity": "sha512-eGuFFw7Upda+g4p+QHvnW0RyTX/SVeJBDM/gCtMARO0cLuT2HcEKnTPvhjV6aGeqrCB/sbNop0Kszm0jsaWU4A==",
            "dev": true
        },
        "esutils": {
            "version": "2.0.2",
            "resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz",
            "integrity": "sha1-Cr9PHKpbyx96nYrMbepPqqBLrJs=",
            "dev": true
        },
        "event-stream": {
            "version": "3.3.4",
            "resolved": "http://registry.npmjs.org/event-stream/-/event-stream-3.3.4.tgz",
            "integrity": "sha1-SrTJoPWlTbkzi0w02Gv86PSzVXE=",
            "dev": true,
            "requires": {
                "duplexer": "0.1.1",
                "from": "0.1.7",
                "map-stream": "0.1.0",
                "pause-stream": "0.0.11",
                "split": "0.3.3",
                "stream-combiner": "0.0.4",
                "through": "2.3.8"
            }
        },
        "expand-brackets": {
            "version": "0.1.5",
            "resolved": "https://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz",
            "integrity": "sha1-3wcoTjQqgHzXM6xa9yQR5YHRF3s=",
            "dev": true,
            "requires": {
                "is-posix-bracket": "0.1.1"
            }
        },
        "expand-range": {
            "version": "1.8.2",
            "resolved": "https://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz",
            "integrity": "sha1-opnv/TNf4nIeuujiV+x5ZE/IUzc=",
            "dev": true,
            "requires": {
                "fill-range": "2.2.4"
            }
        },
        "extend": {
            "version": "3.0.2",
            "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
            "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==",
            "dev": true
        },
        "extend-shallow": {
            "version": "1.1.4",
            "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-1.1.4.tgz",
            "integrity": "sha1-Gda/lN/AnXa6cR85uHLSH/TdkHE=",
            "dev": true,
            "requires": {
                "kind-of": "1.1.0"
            }
        },
        "extglob": {
            "version": "0.3.2",
            "resolved": "https://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz",
            "integrity": "sha1-Lhj/PS9JqydlzskCPwEdqo2DSaE=",
            "dev": true,
            "requires": {
                "is-extglob": "1.0.0"
            },
            "dependencies": {
                "is-extglob": {
                    "version": "1.0.0",
                    "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz",
                    "integrity": "sha1-rEaBd8SUNAWgkvyPKXYMb/xiBsA=",
                    "dev": true
                }
            }
        },
        "extsprintf": {
            "version": "1.3.0",
            "resolved": "https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz",
            "integrity": "sha1-lpGEQOMEGnpBT4xS48V06zw+HgU=",
            "dev": true
        },
        "fast-deep-equal": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.1.0.tgz",
            "integrity": "sha1-wFNHeBfIa1HaqFPIHgWbcz0CNhQ=",
            "dev": true
        },
        "fast-json-stable-stringify": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz",
            "integrity": "sha1-1RQsDK7msRifh9OnYREGT4bIu/I=",
            "dev": true
        },
        "fd-slicer": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.1.0.tgz",
            "integrity": "sha1-JcfInLH5B3+IkbvmHY85Dq4lbx4=",
            "dev": true,
            "requires": {
                "pend": "1.2.0"
            }
        },
        "filename-regex": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/filename-regex/-/filename-regex-2.0.1.tgz",
            "integrity": "sha1-wcS5vuPglyXdsQa3XB4wH+LxiyY=",
            "dev": true
        },
        "fill-range": {
            "version": "2.2.4",
            "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-2.2.4.tgz",
            "integrity": "sha512-cnrcCbj01+j2gTG921VZPnHbjmdAf8oQV/iGeV2kZxGSyfYjjTyY79ErsK1WJWMpw6DaApEX72binqJE+/d+5Q==",
            "dev": true,
            "requires": {
                "is-number": "2.1.0",
                "isobject": "2.1.0",
                "randomatic": "3.1.0",
                "repeat-element": "1.1.3",
                "repeat-string": "1.6.1"
            }
        },
        "first-chunk-stream": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/first-chunk-stream/-/first-chunk-stream-1.0.0.tgz",
            "integrity": "sha1-Wb+1DNkF9g18OUzT2ayqtOatk04=",
            "dev": true
        },
        "for-in": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz",
            "integrity": "sha1-gQaNKVqBQuwKxybG4iAMMPttXoA=",
            "dev": true
        },
        "for-own": {
            "version": "0.1.5",
            "resolved": "https://registry.npmjs.org/for-own/-/for-own-0.1.5.tgz",
            "integrity": "sha1-UmXGgaTylNq78XyVCbZ2OqhFEM4=",
            "dev": true,
            "requires": {
                "for-in": "1.0.2"
            }
        },
        "forever-agent": {
            "version": "0.6.1",
            "resolved": "https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz",
            "integrity": "sha1-+8cfDEGt6zf5bFd60e1C2P2sypE=",
            "dev": true
        },
        "form-data": {
            "version": "2.3.2",
            "resolved": "https://registry.npmjs.org/form-data/-/form-data-2.3.2.tgz",
            "integrity": "sha1-SXBJi+YEwgwAXU9cI67NIda0kJk=",
            "dev": true,
            "requires": {
                "asynckit": "0.4.0",
                "combined-stream": "1.0.6",
                "mime-types": "2.1.20"
            }
        },
        "from": {
            "version": "0.1.7",
            "resolved": "https://registry.npmjs.org/from/-/from-0.1.7.tgz",
            "integrity": "sha1-g8YK/Fi5xWmXAH7Rp2izqzA6RP4=",
            "dev": true
        },
        "fs.realpath": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
            "integrity": "sha1-FQStJSMVjKpA20onh8sBQRmU6k8=",
            "dev": true
        },
        "fstream": {
            "version": "1.0.11",
            "resolved": "https://registry.npmjs.org/fstream/-/fstream-1.0.11.tgz",
            "integrity": "sha1-XB+x8RdHcRTwYyoOtLcbPLD9MXE=",
            "dev": true,
            "requires": {
                "graceful-fs": "4.1.11",
                "inherits": "2.0.3",
                "mkdirp": "0.5.1",
                "rimraf": "2.6.2"
            }
        },
        "getpass": {
            "version": "0.1.7",
            "resolved": "https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz",
            "integrity": "sha1-Xv+OPmhNVprkyysSgmBOi6YhSfo=",
            "dev": true,
            "requires": {
                "assert-plus": "1.0.0"
            }
        },
        "glob": {
            "version": "7.1.3",
            "resolved": "https://registry.npmjs.org/glob/-/glob-7.1.3.tgz",
            "integrity": "sha512-vcfuiIxogLV4DlGBHIUOwI0IbrJ8HWPc4MU7HzviGeNho/UJDfi6B5p3sHeWIQ0KGIU0Jpxi5ZHxemQfLkkAwQ==",
            "dev": true,
            "requires": {
                "fs.realpath": "1.0.0",
                "inflight": "1.0.6",
                "inherits": "2.0.3",
                "minimatch": "3.0.4",
                "once": "1.4.0",
                "path-is-absolute": "1.0.1"
            }
        },
        "glob-base": {
            "version": "0.3.0",
            "resolved": "https://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz",
            "integrity": "sha1-27Fk9iIbHAscz4Kuoyi0l98Oo8Q=",
            "dev": true,
            "requires": {
                "glob-parent": "2.0.0",
                "is-glob": "2.0.1"
            },
            "dependencies": {
                "glob-parent": {
                    "version": "2.0.0",
                    "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz",
                    "integrity": "sha1-gTg9ctsFT8zPUzbaqQLxgvbtuyg=",
                    "dev": true,
                    "requires": {
                        "is-glob": "2.0.1"
                    }
                },
                "is-extglob": {
                    "version": "1.0.0",
                    "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz",
                    "integrity": "sha1-rEaBd8SUNAWgkvyPKXYMb/xiBsA=",
                    "dev": true
                },
                "is-glob": {
                    "version": "2.0.1",
                    "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz",
                    "integrity": "sha1-0Jb5JqPe1WAPP9/ZEZjLCIjC2GM=",
                    "dev": true,
                    "requires": {
                        "is-extglob": "1.0.0"
                    }
                }
            }
        },
        "glob-parent": {
            "version": "3.1.0",
            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-3.1.0.tgz",
            "integrity": "sha1-nmr2KZ2NO9K9QEMIMr0RPfkGxa4=",
            "dev": true,
            "requires": {
                "is-glob": "3.1.0",
                "path-dirname": "1.0.2"
            }
        },
        "glob-stream": {
            "version": "5.3.5",
            "resolved": "https://registry.npmjs.org/glob-stream/-/glob-stream-5.3.5.tgz",
            "integrity": "sha1-pVZlqajM3EGRWofHAeMtTgFvrSI=",
            "dev": true,
            "requires": {
                "extend": "3.0.2",
                "glob": "5.0.15",
                "glob-parent": "3.1.0",
                "micromatch": "2.3.11",
                "ordered-read-streams": "0.3.0",
                "through2": "0.6.5",
                "to-absolute-glob": "0.1.1",
                "unique-stream": "2.2.1"
            },
            "dependencies": {
                "glob": {
                    "version": "5.0.15",
                    "resolved": "https://registry.npmjs.org/glob/-/glob-5.0.15.tgz",
                    "integrity": "sha1-G8k2ueAvSmA/zCIuz3Yz0wuLk7E=",
                    "dev": true,
                    "requires": {
                        "inflight": "1.0.6",
                        "inherits": "2.0.3",
                        "minimatch": "3.0.4",
                        "once": "1.4.0",
                        "path-is-absolute": "1.0.1"
                    }
                },
                "isarray": {
                    "version": "0.0.1",
                    "resolved": "https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz",
                    "integrity": "sha1-ihis/Kmo9Bd+Cav8YDiTmwXR7t8=",
                    "dev": true
                },
                "readable-stream": {
                    "version": "1.0.34",
                    "resolved": "http://registry.npmjs.org/readable-stream/-/readable-stream-1.0.34.tgz",
                    "integrity": "sha1-Elgg40vIQtLyqq+v5MKRbuMsFXw=",
                    "dev": true,
                    "requires": {
                        "core-util-is": "1.0.2",
                        "inherits": "2.0.3",
                        "isarray": "0.0.1",
                        "string_decoder": "0.10.31"
                    }
                },
                "string_decoder": {
                    "version": "0.10.31",
                    "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz",
                    "integrity": "sha1-YuIDvEF2bGwoyfyEMB2rHFMQ+pQ=",
                    "dev": true
                },
                "through2": {
                    "version": "0.6.5",
                    "resolved": "https://registry.npmjs.org/through2/-/through2-0.6.5.tgz",
                    "integrity": "sha1-QaucZ7KdVyCQcUEOHXp6lozTrUg=",
                    "dev": true,
                    "requires": {
                        "readable-stream": "1.0.34",
                        "xtend": "4.0.1"
                    }
                }
            }
        },
        "graceful-fs": {
            "version": "4.1.11",
            "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz",
            "integrity": "sha1-Dovf5NHduIVNZOBOp8AOKgJuVlg=",
            "dev": true
        },
        "growl": {
            "version": "1.10.3",
            "resolved": "https://registry.npmjs.org/growl/-/growl-1.10.3.tgz",
            "integrity": "sha512-hKlsbA5Vu3xsh1Cg3J7jSmX/WaW6A5oBeqzM88oNbCRQFz+zUaXm6yxS4RVytp1scBoJzSYl4YAEOQIt6O8V1Q==",
            "dev": true
        },
        "gulp-chmod": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/gulp-chmod/-/gulp-chmod-2.0.0.tgz",
            "integrity": "sha1-AMOQuSigeZslGsz2MaoJ4BzGKZw=",
            "dev": true,
            "requires": {
                "deep-assign": "1.0.0",
                "stat-mode": "0.2.2",
                "through2": "2.0.3"
            }
        },
        "gulp-filter": {
            "version": "5.1.0",
            "resolved": "https://registry.npmjs.org/gulp-filter/-/gulp-filter-5.1.0.tgz",
            "integrity": "sha1-oF4Rr/sHz33PQafeHLe2OsN4PnM=",
            "dev": true,
            "requires": {
                "multimatch": "2.1.0",
                "plugin-error": "0.1.2",
                "streamfilter": "1.0.7"
            }
        },
        "gulp-gunzip": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/gulp-gunzip/-/gulp-gunzip-1.0.0.tgz",
            "integrity": "sha1-FbdBFF6Dqcb1CIYkG1fMWHHxUak=",
            "dev": true,
            "requires": {
                "through2": "0.6.5",
                "vinyl": "0.4.6"
            },
            "dependencies": {
                "isarray": {
                    "version": "0.0.1",
                    "resolved": "https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz",
                    "integrity": "sha1-ihis/Kmo9Bd+Cav8YDiTmwXR7t8=",
                    "dev": true
                },
                "readable-stream": {
                    "version": "1.0.34",
                    "resolved": "http://registry.npmjs.org/readable-stream/-/readable-stream-1.0.34.tgz",
                    "integrity": "sha1-Elgg40vIQtLyqq+v5MKRbuMsFXw=",
                    "dev": true,
                    "requires": {
                        "core-util-is": "1.0.2",
                        "inherits": "2.0.3",
                        "isarray": "0.0.1",
                        "string_decoder": "0.10.31"
                    }
                },
                "string_decoder": {
                    "version": "0.10.31",
                    "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz",
                    "integrity": "sha1-YuIDvEF2bGwoyfyEMB2rHFMQ+pQ=",
                    "dev": true
                },
                "through2": {
                    "version": "0.6.5",
                    "resolved": "https://registry.npmjs.org/through2/-/through2-0.6.5.tgz",
                    "integrity": "sha1-QaucZ7KdVyCQcUEOHXp6lozTrUg=",
                    "dev": true,
                    "requires": {
                        "readable-stream": "1.0.34",
                        "xtend": "4.0.1"
                    }
                }
            }
        },
        "gulp-remote-src-vscode": {
            "version": "0.5.0",
            "resolved": "https://registry.npmjs.org/gulp-remote-src-vscode/-/gulp-remote-src-vscode-0.5.0.tgz",
            "integrity": "sha512-/9vtSk9eI9DEWCqzGieglPqmx0WUQ9pwPHyHFpKmfxqdgqGJC2l0vFMdYs54hLdDsMDEZFLDL2J4ikjc4hQ5HQ==",
            "dev": true,
            "requires": {
                "event-stream": "3.3.4",
                "node.extend": "1.1.6",
                "request": "2.88.0",
                "through2": "2.0.3",
                "vinyl": "2.2.0"
            },
            "dependencies": {
                "clone": {
                    "version": "2.1.2",
                    "resolved": "https://registry.npmjs.org/clone/-/clone-2.1.2.tgz",
                    "integrity": "sha1-G39Ln1kfHo+DZwQBYANFoCiHQ18=",
                    "dev": true
                },
                "clone-stats": {
                    "version": "1.0.0",
                    "resolved": "https://registry.npmjs.org/clone-stats/-/clone-stats-1.0.0.tgz",
                    "integrity": "sha1-s3gt/4u1R04Yuba/D9/ngvh3doA=",
                    "dev": true
                },
                "vinyl": {
                    "version": "2.2.0",
                    "resolved": "https://registry.npmjs.org/vinyl/-/vinyl-2.2.0.tgz",
                    "integrity": "sha512-MBH+yP0kC/GQ5GwBqrTPTzEfiiLjta7hTtvQtbxBgTeSXsmKQRQecjibMbxIXzVT3Y9KJK+drOz1/k+vsu8Nkg==",
                    "dev": true,
                    "requires": {
                        "clone": "2.1.2",
                        "clone-buffer": "1.0.0",
                        "clone-stats": "1.0.0",
                        "cloneable-readable": "1.1.2",
                        "remove-trailing-separator": "1.1.0",
                        "replace-ext": "1.0.0"
                    }
                }
            }
        },
        "gulp-sourcemaps": {
            "version": "1.6.0",
            "resolved": "https://registry.npmjs.org/gulp-sourcemaps/-/gulp-sourcemaps-1.6.0.tgz",
            "integrity": "sha1-uG/zSdgBzrVuHZ59x7vLS33uYAw=",
            "dev": true,
            "requires": {
                "convert-source-map": "1.5.1",
                "graceful-fs": "4.1.11",
                "strip-bom": "2.0.0",
                "through2": "2.0.3",
                "vinyl": "1.2.0"
            },
            "dependencies": {
                "clone": {
                    "version": "1.0.4",
                    "resolved": "https://registry.npmjs.org/clone/-/clone-1.0.4.tgz",
                    "integrity": "sha1-2jCcwmPfFZlMaIypAheco8fNfH4=",
                    "dev": true
                },
                "replace-ext": {
                    "version": "0.0.1",
                    "resolved": "https://registry.npmjs.org/replace-ext/-/replace-ext-0.0.1.tgz",
                    "integrity": "sha1-KbvZIHinOfC8zitO5B6DeVNSKSQ=",
                    "dev": true
                },
                "vinyl": {
                    "version": "1.2.0",
                    "resolved": "https://registry.npmjs.org/vinyl/-/vinyl-1.2.0.tgz",
                    "integrity": "sha1-XIgDbPVl5d8FVYv8kR+GVt8hiIQ=",
                    "dev": true,
                    "requires": {
                        "clone": "1.0.4",
                        "clone-stats": "0.0.1",
                        "replace-ext": "0.0.1"
                    }
                }
            }
        },
        "gulp-symdest": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/gulp-symdest/-/gulp-symdest-1.1.0.tgz",
            "integrity": "sha1-wWUyBzLRks5W/ZQnH/oSMjS/KuA=",
            "dev": true,
            "requires": {
                "event-stream": "3.3.4",
                "mkdirp": "0.5.1",
                "queue": "3.1.0",
                "vinyl-fs": "2.4.4"
            }
        },
        "gulp-untar": {
            "version": "0.0.7",
            "resolved": "https://registry.npmjs.org/gulp-untar/-/gulp-untar-0.0.7.tgz",
            "integrity": "sha512-0QfbCH2a1k2qkTLWPqTX+QO4qNsHn3kC546YhAP3/n0h+nvtyGITDuDrYBMDZeW4WnFijmkOvBWa5HshTic1tw==",
            "dev": true,
            "requires": {
                "event-stream": "3.3.4",
                "streamifier": "0.1.1",
                "tar": "2.2.1",
                "through2": "2.0.3",
                "vinyl": "1.2.0"
            },
            "dependencies": {
                "clone": {
                    "version": "1.0.4",
                    "resolved": "https://registry.npmjs.org/clone/-/clone-1.0.4.tgz",
                    "integrity": "sha1-2jCcwmPfFZlMaIypAheco8fNfH4=",
                    "dev": true
                },
                "replace-ext": {
                    "version": "0.0.1",
                    "resolved": "https://registry.npmjs.org/replace-ext/-/replace-ext-0.0.1.tgz",
                    "integrity": "sha1-KbvZIHinOfC8zitO5B6DeVNSKSQ=",
                    "dev": true
                },
                "vinyl": {
                    "version": "1.2.0",
                    "resolved": "https://registry.npmjs.org/vinyl/-/vinyl-1.2.0.tgz",
                    "integrity": "sha1-XIgDbPVl5d8FVYv8kR+GVt8hiIQ=",
                    "dev": true,
                    "requires": {
                        "clone": "1.0.4",
                        "clone-stats": "0.0.1",
                        "replace-ext": "0.0.1"
                    }
                }
            }
        },
        "gulp-vinyl-zip": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/gulp-vinyl-zip/-/gulp-vinyl-zip-2.1.0.tgz",
            "integrity": "sha1-JOQGhdwFtxSZlSRQmeBZAmO+ja0=",
            "dev": true,
            "requires": {
                "event-stream": "3.3.4",
                "queue": "4.5.0",
                "through2": "2.0.3",
                "vinyl": "2.2.0",
                "vinyl-fs": "2.4.4",
                "yauzl": "2.10.0",
                "yazl": "2.4.3"
            },
            "dependencies": {
                "clone": {
                    "version": "2.1.2",
                    "resolved": "https://registry.npmjs.org/clone/-/clone-2.1.2.tgz",
                    "integrity": "sha1-G39Ln1kfHo+DZwQBYANFoCiHQ18=",
                    "dev": true
                },
                "clone-stats": {
                    "version": "1.0.0",
                    "resolved": "https://registry.npmjs.org/clone-stats/-/clone-stats-1.0.0.tgz",
                    "integrity": "sha1-s3gt/4u1R04Yuba/D9/ngvh3doA=",
                    "dev": true
                },
                "queue": {
                    "version": "4.5.0",
                    "resolved": "https://registry.npmjs.org/queue/-/queue-4.5.0.tgz",
                    "integrity": "sha512-DwxpAnqJuoQa+wyDgQuwkSshkhlqIlWEvwvdAY27fDPunZ2cVJzXU4JyjY+5l7zs7oGLaYAQm4MbLOVFAHFBzA==",
                    "dev": true,
                    "requires": {
                        "inherits": "2.0.3"
                    }
                },
                "vinyl": {
                    "version": "2.2.0",
                    "resolved": "https://registry.npmjs.org/vinyl/-/vinyl-2.2.0.tgz",
                    "integrity": "sha512-MBH+yP0kC/GQ5GwBqrTPTzEfiiLjta7hTtvQtbxBgTeSXsmKQRQecjibMbxIXzVT3Y9KJK+drOz1/k+vsu8Nkg==",
                    "dev": true,
                    "requires": {
                        "clone": "2.1.2",
                        "clone-buffer": "1.0.0",
                        "clone-stats": "1.0.0",
                        "cloneable-readable": "1.1.2",
                        "remove-trailing-separator": "1.1.0",
                        "replace-ext": "1.0.0"
                    }
                }
            }
        },
        "har-schema": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz",
            "integrity": "sha1-qUwiJOvKwEeCoNkDVSHyRzW37JI=",
            "dev": true
        },
        "har-validator": {
            "version": "5.1.0",
            "resolved": "https://registry.npmjs.org/har-validator/-/har-validator-5.1.0.tgz",
            "integrity": "sha512-+qnmNjI4OfH2ipQ9VQOw23bBd/ibtfbVdK2fYbY4acTDqKTW/YDp9McimZdDbG8iV9fZizUqQMD5xvriB146TA==",
            "dev": true,
            "requires": {
                "ajv": "5.5.2",
                "har-schema": "2.0.0"
            }
        },
        "has-ansi": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz",
            "integrity": "sha1-NPUEnOHs3ysGSa8+8k5F7TVBbZE=",
            "dev": true,
            "requires": {
                "ansi-regex": "2.1.1"
            }
        },
        "has-flag": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz",
            "integrity": "sha1-tdRU3CGZriJWmfNGfloH87lVuv0=",
            "dev": true
        },
        "he": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/he/-/he-1.1.1.tgz",
            "integrity": "sha1-k0EP0hsAlzUVH4howvJx80J+I/0=",
            "dev": true
        },
        "http-signature": {
            "version": "1.2.0",
            "resolved": "https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz",
            "integrity": "sha1-muzZJRFHcvPZW2WmCruPfBj7rOE=",
            "dev": true,
            "requires": {
                "assert-plus": "1.0.0",
                "jsprim": "1.4.1",
                "sshpk": "1.14.2"
            }
        },
        "inflight": {
            "version": "1.0.6",
            "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
            "integrity": "sha1-Sb1jMdfQLQwJvJEKEHW6gWW1bfk=",
            "dev": true,
            "requires": {
                "once": "1.4.0",
                "wrappy": "1.0.2"
            }
        },
        "inherits": {
            "version": "2.0.3",
            "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
            "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4=",
            "dev": true
        },
        "is": {
            "version": "3.2.1",
            "resolved": "https://registry.npmjs.org/is/-/is-3.2.1.tgz",
            "integrity": "sha1-0Kwq1V63sL7JJqUmb2xmKqqD3KU=",
            "dev": true
        },
        "is-buffer": {
            "version": "1.1.6",
            "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz",
            "integrity": "sha512-NcdALwpXkTm5Zvvbk7owOUSvVvBKDgKP5/ewfXEznmQFfs4ZRmanOeKBTjRVjka3QFoN6XJ+9F3USqfHqTaU5w==",
            "dev": true
        },
        "is-dotfile": {
            "version": "1.0.3",
            "resolved": "https://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.3.tgz",
            "integrity": "sha1-pqLzL/0t+wT1yiXs0Pa4PPeYoeE=",
            "dev": true
        },
        "is-equal-shallow": {
            "version": "0.1.3",
            "resolved": "https://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz",
            "integrity": "sha1-IjgJj8Ih3gvPpdnqxMRdY4qhxTQ=",
            "dev": true,
            "requires": {
                "is-primitive": "2.0.0"
            }
        },
        "is-extendable": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz",
            "integrity": "sha1-YrEQ4omkcUGOPsNqYX1HLjAd/Ik=",
            "dev": true
        },
        "is-extglob": {
            "version": "2.1.1",
            "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
            "integrity": "sha1-qIwCU1eR8C7TfHahueqXc8gz+MI=",
            "dev": true
        },
        "is-glob": {
            "version": "3.1.0",
            "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-3.1.0.tgz",
            "integrity": "sha1-e6WuJCF4BKxwcHuWkiVnSGzD6Eo=",
            "dev": true,
            "requires": {
                "is-extglob": "2.1.1"
            }
        },
        "is-number": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz",
            "integrity": "sha1-Afy7s5NGOlSPL0ZszhbezknbkI8=",
            "dev": true,
            "requires": {
                "kind-of": "3.2.2"
            },
            "dependencies": {
                "kind-of": {
                    "version": "3.2.2",
                    "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
                    "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
                    "dev": true,
                    "requires": {
                        "is-buffer": "1.1.6"
                    }
                }
            }
        },
        "is-obj": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/is-obj/-/is-obj-1.0.1.tgz",
            "integrity": "sha1-PkcprB9f3gJc19g6iW2rn09n2w8=",
            "dev": true
        },
        "is-posix-bracket": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz",
            "integrity": "sha1-MzTceXdDaOkvAW5vvAqI9c1ua8Q=",
            "dev": true
        },
        "is-primitive": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz",
            "integrity": "sha1-IHurkWOEmcB7Kt8kCkGochADRXU=",
            "dev": true
        },
        "is-stream": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz",
            "integrity": "sha1-EtSj3U5o4Lec6428hBc66A2RykQ=",
            "dev": true
        },
        "is-typedarray": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz",
            "integrity": "sha1-5HnICFjfDBsR3dppQPlgEfzaSpo=",
            "dev": true
        },
        "is-utf8": {
            "version": "0.2.1",
            "resolved": "https://registry.npmjs.org/is-utf8/-/is-utf8-0.2.1.tgz",
            "integrity": "sha1-Sw2hRCEE0bM2NA6AeX6GXPOffXI=",
            "dev": true
        },
        "is-valid-glob": {
            "version": "0.3.0",
            "resolved": "https://registry.npmjs.org/is-valid-glob/-/is-valid-glob-0.3.0.tgz",
            "integrity": "sha1-1LVcafUYhvm2XHDWwmItN+KfSP4=",
            "dev": true
        },
        "isarray": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
            "integrity": "sha1-u5NdSFgsuhaMBoNJV6VKPgcSTxE=",
            "dev": true
        },
        "isobject": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz",
            "integrity": "sha1-8GVWEJaj8dou9GJy+BXIQNh+DIk=",
            "dev": true,
            "requires": {
                "isarray": "1.0.0"
            }
        },
        "isstream": {
            "version": "0.1.2",
            "resolved": "https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz",
            "integrity": "sha1-R+Y/evVa+m+S4VAOaQ64uFKcCZo=",
            "dev": true
        },
        "js-tokens": {
            "version": "3.0.2",
            "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz",
            "integrity": "sha1-mGbfOVECEw449/mWvOtlRDIJwls=",
            "dev": true
        },
        "js-yaml": {
            "version": "3.12.0",
            "resolved": "https://registry.npmjs.org/js-yaml/-/js-yaml-3.12.0.tgz",
            "integrity": "sha512-PIt2cnwmPfL4hKNwqeiuz4bKfnzHTBv6HyVgjahA6mPLwPDzjDWrplJBMjHUFxku/N3FlmrbyPclad+I+4mJ3A==",
            "dev": true,
            "requires": {
                "argparse": "1.0.10",
                "esprima": "4.0.1"
            }
        },
        "jsbn": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz",
            "integrity": "sha1-peZUwuWi3rXyAdls77yoDA7y9RM=",
            "dev": true,
            "optional": true
        },
        "json-schema": {
            "version": "0.2.3",
            "resolved": "https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz",
            "integrity": "sha1-tIDIkuWaLwWVTOcnvT8qTogvnhM=",
            "dev": true
        },
        "json-schema-traverse": {
            "version": "0.3.1",
            "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz",
            "integrity": "sha1-NJptRMU6Ud6JtAgFxdXlm0F9M0A=",
            "dev": true
        },
        "json-stable-stringify": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/json-stable-stringify/-/json-stable-stringify-1.0.1.tgz",
            "integrity": "sha1-mnWdOcXy/1A/1TAGRu1EX4jE+a8=",
            "dev": true,
            "requires": {
                "jsonify": "0.0.0"
            }
        },
        "json-stringify-safe": {
            "version": "5.0.1",
            "resolved": "https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz",
            "integrity": "sha1-Epai1Y/UXxmg9s4B1lcB4sc1tus=",
            "dev": true
        },
        "jsonify": {
            "version": "0.0.0",
            "resolved": "https://registry.npmjs.org/jsonify/-/jsonify-0.0.0.tgz",
            "integrity": "sha1-LHS27kHZPKUbe1qu6PUDYx0lKnM=",
            "dev": true
        },
        "jsprim": {
            "version": "1.4.1",
            "resolved": "https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz",
            "integrity": "sha1-MT5mvB5cwG5Di8G3SZwuXFastqI=",
            "dev": true,
            "requires": {
                "assert-plus": "1.0.0",
                "extsprintf": "1.3.0",
                "json-schema": "0.2.3",
                "verror": "1.10.0"
            }
        },
        "kind-of": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-1.1.0.tgz",
            "integrity": "sha1-FAo9LUGjbS78+pN3tiwk+ElaXEQ=",
            "dev": true
        },
        "lazystream": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/lazystream/-/lazystream-1.0.0.tgz",
            "integrity": "sha1-9plf4PggOS9hOWvolGJAe7dxaOQ=",
            "dev": true,
            "requires": {
                "readable-stream": "2.3.6"
            }
        },
        "lodash.isequal": {
            "version": "4.5.0",
            "resolved": "https://registry.npmjs.org/lodash.isequal/-/lodash.isequal-4.5.0.tgz",
            "integrity": "sha1-QVxEePK8wwEgwizhDtMib30+GOA=",
            "dev": true
        },
        "map-stream": {
            "version": "0.1.0",
            "resolved": "https://registry.npmjs.org/map-stream/-/map-stream-0.1.0.tgz",
            "integrity": "sha1-5WqpTEyAVaFkBKBnS3jyFffI4ZQ=",
            "dev": true
        },
        "math-random": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/math-random/-/math-random-1.0.1.tgz",
            "integrity": "sha1-izqsWIuKZuSXXjzepn97sylgH6w=",
            "dev": true
        },
        "merge-stream": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/merge-stream/-/merge-stream-1.0.1.tgz",
            "integrity": "sha1-QEEgLVCKNCugAXQAjfDCUbjBNeE=",
            "dev": true,
            "requires": {
                "readable-stream": "2.3.6"
            }
        },
        "micromatch": {
            "version": "2.3.11",
            "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz",
            "integrity": "sha1-hmd8l9FyCzY0MdBNDRUpO9OMFWU=",
            "dev": true,
            "requires": {
                "arr-diff": "2.0.0",
                "array-unique": "0.2.1",
                "braces": "1.8.5",
                "expand-brackets": "0.1.5",
                "extglob": "0.3.2",
                "filename-regex": "2.0.1",
                "is-extglob": "1.0.0",
                "is-glob": "2.0.1",
                "kind-of": "3.2.2",
                "normalize-path": "2.1.1",
                "object.omit": "2.0.1",
                "parse-glob": "3.0.4",
                "regex-cache": "0.4.4"
            },
            "dependencies": {
                "arr-diff": {
                    "version": "2.0.0",
                    "resolved": "https://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz",
                    "integrity": "sha1-jzuCf5Vai9ZpaX5KQlasPOrjVs8=",
                    "dev": true,
                    "requires": {
                        "arr-flatten": "1.1.0"
                    }
                },
                "is-extglob": {
                    "version": "1.0.0",
                    "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz",
                    "integrity": "sha1-rEaBd8SUNAWgkvyPKXYMb/xiBsA=",
                    "dev": true
                },
                "is-glob": {
                    "version": "2.0.1",
                    "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz",
                    "integrity": "sha1-0Jb5JqPe1WAPP9/ZEZjLCIjC2GM=",
                    "dev": true,
                    "requires": {
                        "is-extglob": "1.0.0"
                    }
                },
                "kind-of": {
                    "version": "3.2.2",
                    "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
                    "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
                    "dev": true,
                    "requires": {
                        "is-buffer": "1.1.6"
                    }
                }
            }
        },
        "mime-db": {
            "version": "1.36.0",
            "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.36.0.tgz",
            "integrity": "sha512-L+xvyD9MkoYMXb1jAmzI/lWYAxAMCPvIBSWur0PZ5nOf5euahRLVqH//FKW9mWp2lkqUgYiXPgkzfMUFi4zVDw==",
            "dev": true
        },
        "mime-types": {
            "version": "2.1.20",
            "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.20.tgz",
            "integrity": "sha512-HrkrPaP9vGuWbLK1B1FfgAkbqNjIuy4eHlIYnFi7kamZyLLrGlo2mpcx0bBmNpKqBtYtAfGbodDddIgddSJC2A==",
            "dev": true,
            "requires": {
                "mime-db": "1.36.0"
            }
        },
        "minimatch": {
            "version": "3.0.4",
            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz",
            "integrity": "sha512-yJHVQEhyqPLUTgt9B83PXu6W3rx4MvvHvSUvToogpwoGDOUQ+yDrR0HRot+yOCdCO7u4hX3pWft6kWBBcqh0UA==",
            "dev": true,
            "requires": {
                "brace-expansion": "1.1.11"
            }
        },
        "minimist": {
            "version": "0.0.8",
            "resolved": "https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz",
            "integrity": "sha1-hX/Kv8M5fSYluCKCYuhqp6ARsF0=",
            "dev": true
        },
        "mkdirp": {
            "version": "0.5.1",
            "resolved": "http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz",
            "integrity": "sha1-MAV0OOrGz3+MR2fzhkjWaX11yQM=",
            "dev": true,
            "requires": {
                "minimist": "0.0.8"
            }
        },
        "mocha": {
            "version": "4.1.0",
            "resolved": "https://registry.npmjs.org/mocha/-/mocha-4.1.0.tgz",
            "integrity": "sha512-0RVnjg1HJsXY2YFDoTNzcc1NKhYuXKRrBAG2gDygmJJA136Cs2QlRliZG1mA0ap7cuaT30mw16luAeln+4RiNA==",
            "dev": true,
            "requires": {
                "browser-stdout": "1.3.0",
                "commander": "2.11.0",
                "debug": "3.1.0",
                "diff": "3.3.1",
                "escape-string-regexp": "1.0.5",
                "glob": "7.1.2",
                "growl": "1.10.3",
                "he": "1.1.1",
                "mkdirp": "0.5.1",
                "supports-color": "4.4.0"
            },
            "dependencies": {
                "commander": {
                    "version": "2.11.0",
                    "resolved": "https://registry.npmjs.org/commander/-/commander-2.11.0.tgz",
                    "integrity": "sha512-b0553uYA5YAEGgyYIGYROzKQ7X5RAqedkfjiZxwi0kL1g3bOaBNNZfYkzt/CL0umgD5wc9Jec2FbB98CjkMRvQ==",
                    "dev": true
                },
                "diff": {
                    "version": "3.3.1",
                    "resolved": "https://registry.npmjs.org/diff/-/diff-3.3.1.tgz",
                    "integrity": "sha512-MKPHZDMB0o6yHyDryUOScqZibp914ksXwAMYMTHj6KO8UeKsRYNJD3oNCKjTqZon+V488P7N/HzXF8t7ZR95ww==",
                    "dev": true
                },
                "glob": {
                    "version": "7.1.2",
                    "resolved": "https://registry.npmjs.org/glob/-/glob-7.1.2.tgz",
                    "integrity": "sha512-MJTUg1kjuLeQCJ+ccE4Vpa6kKVXkPYJ2mOCQyUuKLcLQsdrMCpBPUi8qVE6+YuaJkozeA9NusTAw3hLr8Xe5EQ==",
                    "dev": true,
                    "requires": {
                        "fs.realpath": "1.0.0",
                        "inflight": "1.0.6",
                        "inherits": "2.0.3",
                        "minimatch": "3.0.4",
                        "once": "1.4.0",
                        "path-is-absolute": "1.0.1"
                    }
                },
                "has-flag": {
                    "version": "2.0.0",
                    "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz",
                    "integrity": "sha1-6CB68cx7MNRGzHC3NLXovhj4jVE=",
                    "dev": true
                },
                "supports-color": {
                    "version": "4.4.0",
                    "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.4.0.tgz",
                    "integrity": "sha512-rKC3+DyXWgK0ZLKwmRsrkyHVZAjNkfzeehuFWdGGcqGDTZFH73+RH6S/RDAAxl9GusSjZSUWYLmT9N5pzXFOXQ==",
                    "dev": true,
                    "requires": {
                        "has-flag": "2.0.0"
                    }
                }
            }
        },
        "ms": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
            "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g=",
            "dev": true
        },
        "multimatch": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/multimatch/-/multimatch-2.1.0.tgz",
            "integrity": "sha1-nHkGoi+0wCkZ4vX3UWG0zb1LKis=",
            "dev": true,
            "requires": {
                "array-differ": "1.0.0",
                "array-union": "1.0.2",
                "arrify": "1.0.1",
                "minimatch": "3.0.4"
            }
        },
        "node.extend": {
            "version": "1.1.6",
            "resolved": "https://registry.npmjs.org/node.extend/-/node.extend-1.1.6.tgz",
            "integrity": "sha1-p7iCyC1sk6SGOlUEvV3o7IYli5Y=",
            "dev": true,
            "requires": {
                "is": "3.2.1"
            }
        },
        "normalize-path": {
            "version": "2.1.1",
            "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz",
            "integrity": "sha1-GrKLVW4Zg2Oowab35vogE3/mrtk=",
            "dev": true,
            "requires": {
                "remove-trailing-separator": "1.1.0"
            }
        },
        "oauth-sign": {
            "version": "0.9.0",
            "resolved": "https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz",
            "integrity": "sha512-fexhUFFPTGV8ybAtSIGbV6gOkSv8UtRbDBnAyLQw4QPKkgNlsH2ByPGtMUqdWkos6YCRmAqViwgZrJc/mRDzZQ==",
            "dev": true
        },
        "object-assign": {
            "version": "4.1.1",
            "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
            "integrity": "sha1-IQmtx5ZYh8/AXLvUQsrIv7s2CGM=",
            "dev": true
        },
        "object.omit": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/object.omit/-/object.omit-2.0.1.tgz",
            "integrity": "sha1-Gpx0SCnznbuFjHbKNXmuKlTr0fo=",
            "dev": true,
            "requires": {
                "for-own": "0.1.5",
                "is-extendable": "0.1.1"
            }
        },
        "once": {
            "version": "1.4.0",
            "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
            "integrity": "sha1-WDsap3WWHUsROsF9nFC6753Xa9E=",
            "dev": true,
            "requires": {
                "wrappy": "1.0.2"
            }
        },
        "ordered-read-streams": {
            "version": "0.3.0",
            "resolved": "https://registry.npmjs.org/ordered-read-streams/-/ordered-read-streams-0.3.0.tgz",
            "integrity": "sha1-cTfmmzKYuzQiR6G77jiByA4v14s=",
            "dev": true,
            "requires": {
                "is-stream": "1.1.0",
                "readable-stream": "2.3.6"
            }
        },
        "parse-glob": {
            "version": "3.0.4",
            "resolved": "https://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz",
            "integrity": "sha1-ssN2z7EfNVE7rdFz7wu246OIORw=",
            "dev": true,
            "requires": {
                "glob-base": "0.3.0",
                "is-dotfile": "1.0.3",
                "is-extglob": "1.0.0",
                "is-glob": "2.0.1"
            },
            "dependencies": {
                "is-extglob": {
                    "version": "1.0.0",
                    "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz",
                    "integrity": "sha1-rEaBd8SUNAWgkvyPKXYMb/xiBsA=",
                    "dev": true
                },
                "is-glob": {
                    "version": "2.0.1",
                    "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz",
                    "integrity": "sha1-0Jb5JqPe1WAPP9/ZEZjLCIjC2GM=",
                    "dev": true,
                    "requires": {
                        "is-extglob": "1.0.0"
                    }
                }
            }
        },
        "path-dirname": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/path-dirname/-/path-dirname-1.0.2.tgz",
            "integrity": "sha1-zDPSTVJeCZpTiMAzbG4yuRYGCeA=",
            "dev": true
        },
        "path-is-absolute": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
            "integrity": "sha1-F0uSaHNVNP+8es5r9TpanhtcX18=",
            "dev": true
        },
        "path-parse": {
            "version": "1.0.6",
            "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.6.tgz",
            "integrity": "sha512-GSmOT2EbHrINBf9SR7CDELwlJ8AENk3Qn7OikK4nFYAu3Ote2+JYNVvkpAEQm3/TLNEJFD/xZJjzyxg3KBWOzw==",
            "dev": true
        },
        "pause-stream": {
            "version": "0.0.11",
            "resolved": "https://registry.npmjs.org/pause-stream/-/pause-stream-0.0.11.tgz",
            "integrity": "sha1-/lo0sMvOErWqaitAPuLnO2AvFEU=",
            "dev": true,
            "requires": {
                "through": "2.3.8"
            }
        },
        "pend": {
            "version": "1.2.0",
            "resolved": "https://registry.npmjs.org/pend/-/pend-1.2.0.tgz",
            "integrity": "sha1-elfrVQpng/kRUzH89GY9XI4AelA=",
            "dev": true
        },
        "performance-now": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz",
            "integrity": "sha1-Ywn04OX6kT7BxpMHrjZLSzd8nns=",
            "dev": true
        },
        "plugin-error": {
            "version": "0.1.2",
            "resolved": "https://registry.npmjs.org/plugin-error/-/plugin-error-0.1.2.tgz",
            "integrity": "sha1-O5uzM1zPAPQl4HQ34ZJ2ln2kes4=",
            "dev": true,
            "requires": {
                "ansi-cyan": "0.1.1",
                "ansi-red": "0.1.1",
                "arr-diff": "1.1.0",
                "arr-union": "2.1.0",
                "extend-shallow": "1.1.4"
            }
        },
        "preserve": {
            "version": "0.2.0",
            "resolved": "https://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz",
            "integrity": "sha1-gV7R9uvGWSb4ZbMQwHE7yzMVzks=",
            "dev": true
        },
        "process-nextick-args": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.0.tgz",
            "integrity": "sha512-MtEC1TqN0EU5nephaJ4rAtThHtC86dNN9qCuEhtshvpVBkAW5ZO7BASN9REnF9eoXGcRub+pFuKEpOHE+HbEMw==",
            "dev": true
        },
        "psl": {
            "version": "1.1.29",
            "resolved": "https://registry.npmjs.org/psl/-/psl-1.1.29.tgz",
            "integrity": "sha512-AeUmQ0oLN02flVHXWh9sSJF7mcdFq0ppid/JkErufc3hGIV/AMa8Fo9VgDo/cT2jFdOWoFvHp90qqBH54W+gjQ==",
            "dev": true
        },
        "punycode": {
            "version": "1.4.1",
            "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz",
            "integrity": "sha1-wNWmOycYgArY4esPpSachN1BhF4=",
            "dev": true
        },
        "qs": {
            "version": "6.5.2",
            "resolved": "https://registry.npmjs.org/qs/-/qs-6.5.2.tgz",
            "integrity": "sha512-N5ZAX4/LxJmF+7wN74pUD6qAh9/wnvdQcjq9TZjevvXzSUo7bfmw91saqMjzGS2xq91/odN2dW/WOl7qQHNDGA==",
            "dev": true
        },
        "querystringify": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/querystringify/-/querystringify-2.0.0.tgz",
            "integrity": "sha512-eTPo5t/4bgaMNZxyjWx6N2a6AuE0mq51KWvpc7nU/MAqixcI6v6KrGUKES0HaomdnolQBBXU/++X6/QQ9KL4tw==",
            "dev": true
        },
        "queue": {
            "version": "3.1.0",
            "resolved": "https://registry.npmjs.org/queue/-/queue-3.1.0.tgz",
            "integrity": "sha1-bEnQHwCeIlZ4h4nyv/rGuLmZBYU=",
            "dev": true,
            "requires": {
                "inherits": "2.0.3"
            }
        },
        "randomatic": {
            "version": "3.1.0",
            "resolved": "https://registry.npmjs.org/randomatic/-/randomatic-3.1.0.tgz",
            "integrity": "sha512-KnGPVE0lo2WoXxIZ7cPR8YBpiol4gsSuOwDSg410oHh80ZMp5EiypNqL2K4Z77vJn6lB5rap7IkAmcUlalcnBQ==",
            "dev": true,
            "requires": {
                "is-number": "4.0.0",
                "kind-of": "6.0.2",
                "math-random": "1.0.1"
            },
            "dependencies": {
                "is-number": {
                    "version": "4.0.0",
                    "resolved": "https://registry.npmjs.org/is-number/-/is-number-4.0.0.tgz",
                    "integrity": "sha512-rSklcAIlf1OmFdyAqbnWTLVelsQ58uvZ66S/ZyawjWqIviTWCjg2PzVGw8WUA+nNuPTqb4wgA+NszrJ+08LlgQ==",
                    "dev": true
                },
                "kind-of": {
                    "version": "6.0.2",
                    "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-6.0.2.tgz",
                    "integrity": "sha512-s5kLOcnH0XqDO+FvuaLX8DDjZ18CGFk7VygH40QoKPUQhW4e2rvM0rwUq0t8IQDOwYSeLK01U90OjzBTme2QqA==",
                    "dev": true
                }
            }
        },
        "readable-stream": {
            "version": "2.3.6",
            "resolved": "http://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz",
            "integrity": "sha512-tQtKA9WIAhBF3+VLAseyMqZeBjW0AHJoxOtYqSUZNJxauErmLbVm2FW1y+J/YA9dUrAC39ITejlZWhVIwawkKw==",
            "dev": true,
            "requires": {
                "core-util-is": "1.0.2",
                "inherits": "2.0.3",
                "isarray": "1.0.0",
                "process-nextick-args": "2.0.0",
                "safe-buffer": "5.1.2",
                "string_decoder": "1.1.1",
                "util-deprecate": "1.0.2"
            }
        },
        "regex-cache": {
            "version": "0.4.4",
            "resolved": "https://registry.npmjs.org/regex-cache/-/regex-cache-0.4.4.tgz",
            "integrity": "sha512-nVIZwtCjkC9YgvWkpM55B5rBhBYRZhAaJbgcFYXXsHnbZ9UZI9nnVWYZpBlCqv9ho2eZryPnWrZGsOdPwVWXWQ==",
            "dev": true,
            "requires": {
                "is-equal-shallow": "0.1.3"
            }
        },
        "remove-trailing-separator": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz",
            "integrity": "sha1-wkvOKig62tW8P1jg1IJJuSN52O8=",
            "dev": true
        },
        "repeat-element": {
            "version": "1.1.3",
            "resolved": "https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.3.tgz",
            "integrity": "sha512-ahGq0ZnV5m5XtZLMb+vP76kcAM5nkLqk0lpqAuojSKGgQtn4eRi4ZZGm2olo2zKFH+sMsWaqOCW1dqAnOru72g==",
            "dev": true
        },
        "repeat-string": {
            "version": "1.6.1",
            "resolved": "https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz",
            "integrity": "sha1-jcrkcOHIirwtYA//Sndihtp15jc=",
            "dev": true
        },
        "replace-ext": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/replace-ext/-/replace-ext-1.0.0.tgz",
            "integrity": "sha1-3mMSg3P8v3w8z6TeWkgMRaZ5WOs=",
            "dev": true
        },
        "request": {
            "version": "2.88.0",
            "resolved": "https://registry.npmjs.org/request/-/request-2.88.0.tgz",
            "integrity": "sha512-NAqBSrijGLZdM0WZNsInLJpkJokL72XYjUpnB0iwsRgxh7dB6COrHnTBNwN0E+lHDAJzu7kLAkDeY08z2/A0hg==",
            "dev": true,
            "requires": {
                "aws-sign2": "0.7.0",
                "aws4": "1.8.0",
                "caseless": "0.12.0",
                "combined-stream": "1.0.6",
                "extend": "3.0.2",
                "forever-agent": "0.6.1",
                "form-data": "2.3.2",
                "har-validator": "5.1.0",
                "http-signature": "1.2.0",
                "is-typedarray": "1.0.0",
                "isstream": "0.1.2",
                "json-stringify-safe": "5.0.1",
                "mime-types": "2.1.20",
                "oauth-sign": "0.9.0",
                "performance-now": "2.1.0",
                "qs": "6.5.2",
                "safe-buffer": "5.1.2",
                "tough-cookie": "2.4.3",
                "tunnel-agent": "0.6.0",
                "uuid": "3.3.2"
            }
        },
        "requires-port": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/requires-port/-/requires-port-1.0.0.tgz",
            "integrity": "sha1-kl0mAdOaxIXgkc8NpcbmlNw9yv8=",
            "dev": true
        },
        "resolve": {
            "version": "1.8.1",
            "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.8.1.tgz",
            "integrity": "sha512-AicPrAC7Qu1JxPCZ9ZgCZlY35QgFnNqc+0LtbRNxnVw4TXvjQ72wnuL9JQcEBgXkI9JM8MsT9kaQoHcpCRJOYA==",
            "dev": true,
            "requires": {
                "path-parse": "1.0.6"
            }
        },
        "rimraf": {
            "version": "2.6.2",
            "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-2.6.2.tgz",
            "integrity": "sha512-lreewLK/BlghmxtfH36YYVg1i8IAce4TI7oao75I1g245+6BctqTVQiBP3YUJ9C6DQOXJmkYR9X9fCLtCOJc5w==",
            "dev": true,
            "requires": {
                "glob": "7.1.3"
            }
        },
        "safe-buffer": {
            "version": "5.1.2",
            "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
            "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==",
            "dev": true
        },
        "safer-buffer": {
            "version": "2.1.2",
            "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
            "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==",
            "dev": true
        },
        "semver": {
            "version": "5.5.1",
            "resolved": "https://registry.npmjs.org/semver/-/semver-5.5.1.tgz",
            "integrity": "sha512-PqpAxfrEhlSUWge8dwIp4tZnQ25DIOthpiaHNIthsjEFQD6EvqUKUDM7L8O2rShkFccYo1VjJR0coWfNkCubRw==",
            "dev": true
        },
        "source-map": {
            "version": "0.6.1",
            "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz",
            "integrity": "sha512-UjgapumWlbMhkBgzT7Ykc5YXUT46F0iKu8SGXq0bcwP5dz/h0Plj6enJqjz1Zbq2l5WaqYnrVbwWOWMyF3F47g==",
            "dev": true
        },
        "source-map-support": {
            "version": "0.5.9",
            "resolved": "https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.9.tgz",
            "integrity": "sha512-gR6Rw4MvUlYy83vP0vxoVNzM6t8MUXqNuRsuBmBHQDu1Fh6X015FrLdgoDKcNdkwGubozq0P4N0Q37UyFVr1EA==",
            "dev": true,
            "requires": {
                "buffer-from": "1.1.1",
                "source-map": "0.6.1"
            }
        },
        "split": {
            "version": "0.3.3",
            "resolved": "https://registry.npmjs.org/split/-/split-0.3.3.tgz",
            "integrity": "sha1-zQ7qXmOiEd//frDwkcQTPi0N0o8=",
            "dev": true,
            "requires": {
                "through": "2.3.8"
            }
        },
        "sprintf-js": {
            "version": "1.0.3",
            "resolved": "https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz",
            "integrity": "sha1-BOaSb2YolTVPPdAVIDYzuFcpfiw=",
            "dev": true
        },
        "sshpk": {
            "version": "1.14.2",
            "resolved": "https://registry.npmjs.org/sshpk/-/sshpk-1.14.2.tgz",
            "integrity": "sha1-xvxhZIo9nE52T9P8306hBeSSupg=",
            "dev": true,
            "requires": {
                "asn1": "0.2.4",
                "assert-plus": "1.0.0",
                "bcrypt-pbkdf": "1.0.2",
                "dashdash": "1.14.1",
                "ecc-jsbn": "0.1.2",
                "getpass": "0.1.7",
                "jsbn": "0.1.1",
                "safer-buffer": "2.1.2",
                "tweetnacl": "0.14.5"
            }
        },
        "stat-mode": {
            "version": "0.2.2",
            "resolved": "https://registry.npmjs.org/stat-mode/-/stat-mode-0.2.2.tgz",
            "integrity": "sha1-5sgLYjEj19gM8TLOU480YokHJQI=",
            "dev": true
        },
        "stream-combiner": {
            "version": "0.0.4",
            "resolved": "https://registry.npmjs.org/stream-combiner/-/stream-combiner-0.0.4.tgz",
            "integrity": "sha1-TV5DPBhSYd3mI8o/RMWGvPXErRQ=",
            "dev": true,
            "requires": {
                "duplexer": "0.1.1"
            }
        },
        "stream-shift": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.0.tgz",
            "integrity": "sha1-1cdSgl5TZ+eG944Y5EXqIjoVWVI=",
            "dev": true
        },
        "streamfilter": {
            "version": "1.0.7",
            "resolved": "https://registry.npmjs.org/streamfilter/-/streamfilter-1.0.7.tgz",
            "integrity": "sha512-Gk6KZM+yNA1JpW0KzlZIhjo3EaBJDkYfXtYSbOwNIQ7Zd6006E6+sCFlW1NDvFG/vnXhKmw6TJJgiEQg/8lXfQ==",
            "dev": true,
            "requires": {
                "readable-stream": "2.3.6"
            }
        },
        "streamifier": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/streamifier/-/streamifier-0.1.1.tgz",
            "integrity": "sha1-l+mNj6TRBdYqJpHR3AfoINuN/E8=",
            "dev": true
        },
        "string_decoder": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
            "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
            "dev": true,
            "requires": {
                "safe-buffer": "5.1.2"
            }
        },
        "strip-ansi": {
            "version": "3.0.1",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz",
            "integrity": "sha1-ajhfuIU9lS1f8F0Oiq+UJ43GPc8=",
            "dev": true,
            "requires": {
                "ansi-regex": "2.1.1"
            }
        },
        "strip-bom": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/strip-bom/-/strip-bom-2.0.0.tgz",
            "integrity": "sha1-YhmoVhZSBJHzV4i9vxRHqZx+aw4=",
            "dev": true,
            "requires": {
                "is-utf8": "0.2.1"
            }
        },
        "strip-bom-stream": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/strip-bom-stream/-/strip-bom-stream-1.0.0.tgz",
            "integrity": "sha1-5xRDmFd9Uaa+0PoZlPoF9D/ZiO4=",
            "dev": true,
            "requires": {
                "first-chunk-stream": "1.0.0",
                "strip-bom": "2.0.0"
            }
        },
        "supports-color": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz",
            "integrity": "sha1-U10EXOa2Nj+kARcIRimZXp3zJMc=",
            "dev": true
        },
        "tar": {
            "version": "2.2.1",
            "resolved": "https://registry.npmjs.org/tar/-/tar-2.2.1.tgz",
            "integrity": "sha1-jk0qJWwOIYXGsYrWlK7JaLg8sdE=",
            "dev": true,
            "requires": {
                "block-stream": "0.0.9",
                "fstream": "1.0.11",
                "inherits": "2.0.3"
            }
        },
        "through": {
            "version": "2.3.8",
            "resolved": "https://registry.npmjs.org/through/-/through-2.3.8.tgz",
            "integrity": "sha1-DdTJ/6q8NXlgsbckEV1+Doai4fU=",
            "dev": true
        },
        "through2": {
            "version": "2.0.3",
            "resolved": "https://registry.npmjs.org/through2/-/through2-2.0.3.tgz",
            "integrity": "sha1-AARWmzfHx0ujnEPzzteNGtlBQL4=",
            "dev": true,
            "requires": {
                "readable-stream": "2.3.6",
                "xtend": "4.0.1"
            }
        },
        "through2-filter": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/through2-filter/-/through2-filter-2.0.0.tgz",
            "integrity": "sha1-YLxVoNrLdghdsfna6Zq0P4PWIuw=",
            "dev": true,
            "requires": {
                "through2": "2.0.3",
                "xtend": "4.0.1"
            }
        },
        "to-absolute-glob": {
            "version": "0.1.1",
            "resolved": "https://registry.npmjs.org/to-absolute-glob/-/to-absolute-glob-0.1.1.tgz",
            "integrity": "sha1-HN+kcqnvUMI57maZm2YsoOs5k38=",
            "dev": true,
            "requires": {
                "extend-shallow": "2.0.1"
            },
            "dependencies": {
                "extend-shallow": {
                    "version": "2.0.1",
                    "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
                    "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
                    "dev": true,
                    "requires": {
                        "is-extendable": "0.1.1"
                    }
                }
            }
        },
        "tough-cookie": {
            "version": "2.4.3",
            "resolved": "https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.4.3.tgz",
            "integrity": "sha512-Q5srk/4vDM54WJsJio3XNn6K2sCG+CQ8G5Wz6bZhRZoAe/+TxjWB/GlFAnYEbkYVlON9FMk/fE3h2RLpPXo4lQ==",
            "dev": true,
            "requires": {
                "psl": "1.1.29",
                "punycode": "1.4.1"
            }
        },
        "tslib": {
            "version": "1.9.3",
            "resolved": "https://registry.npmjs.org/tslib/-/tslib-1.9.3.tgz",
            "integrity": "sha512-4krF8scpejhaOgqzBEcGM7yDIEfi0/8+8zDRZhNZZ2kjmHJ4hv3zCbQWxoJGz1iw5U0Jl0nma13xzHXcncMavQ==",
            "dev": true
        },
        "tslint": {
            "version": "5.11.0",
            "resolved": "https://registry.npmjs.org/tslint/-/tslint-5.11.0.tgz",
            "integrity": "sha1-mPMMAurjzecAYgHkwzywi0hYHu0=",
            "dev": true,
            "requires": {
                "babel-code-frame": "6.26.0",
                "builtin-modules": "1.1.1",
                "chalk": "2.4.1",
                "commander": "2.18.0",
                "diff": "3.5.0",
                "glob": "7.1.3",
                "js-yaml": "3.12.0",
                "minimatch": "3.0.4",
                "resolve": "1.8.1",
                "semver": "5.5.1",
                "tslib": "1.9.3",
                "tsutils": "2.29.0"
            }
        },
        "tsutils": {
            "version": "2.29.0",
            "resolved": "https://registry.npmjs.org/tsutils/-/tsutils-2.29.0.tgz",
            "integrity": "sha512-g5JVHCIJwzfISaXpXE1qvNalca5Jwob6FjI4AoPlqMusJ6ftFE7IkkFoMhVLRgK+4Kx3gkzb8UZK5t5yTTvEmA==",
            "dev": true,
            "requires": {
                "tslib": "1.9.3"
            }
        },
        "tunnel-agent": {
            "version": "0.6.0",
            "resolved": "https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz",
            "integrity": "sha1-J6XeoGs2sEoKmWZ3SykIaPD8QP0=",
            "dev": true,
            "requires": {
                "safe-buffer": "5.1.2"
            }
        },
        "tweetnacl": {
            "version": "0.14.5",
            "resolved": "https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz",
            "integrity": "sha1-WuaBd/GS1EViadEIr6k/+HQ/T2Q=",
            "dev": true,
            "optional": true
        },
        "typescript": {
            "version": "2.9.2",
            "resolved": "https://registry.npmjs.org/typescript/-/typescript-2.9.2.tgz",
            "integrity": "sha512-Gr4p6nFNaoufRIY4NMdpQRNmgxVIGMs4Fcu/ujdYk3nAZqk7supzBE9idmvfZIlH/Cuj//dvi+019qEue9lV0w==",
            "dev": true
        },
        "unique-stream": {
            "version": "2.2.1",
            "resolved": "https://registry.npmjs.org/unique-stream/-/unique-stream-2.2.1.tgz",
            "integrity": "sha1-WqADz76Uxf+GbE59ZouxxNuts2k=",
            "dev": true,
            "requires": {
                "json-stable-stringify": "1.0.1",
                "through2-filter": "2.0.0"
            }
        },
        "url-parse": {
            "version": "1.4.3",
            "resolved": "https://registry.npmjs.org/url-parse/-/url-parse-1.4.3.tgz",
            "integrity": "sha512-rh+KuAW36YKo0vClhQzLLveoj8FwPJNu65xLb7Mrt+eZht0IPT0IXgSv8gcMegZ6NvjJUALf6Mf25POlMwD1Fw==",
            "dev": true,
            "requires": {
                "querystringify": "2.0.0",
                "requires-port": "1.0.0"
            }
        },
        "util-deprecate": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
            "integrity": "sha1-RQ1Nyfpw3nMnYvvS1KKJgUGaDM8=",
            "dev": true
        },
        "uuid": {
            "version": "3.3.2",
            "resolved": "https://registry.npmjs.org/uuid/-/uuid-3.3.2.tgz",
            "integrity": "sha512-yXJmeNaw3DnnKAOKJE51sL/ZaYfWJRl1pK9dr19YFCu0ObS231AB1/LbqTKRAQ5kw8A90rA6fr4riOUpTZvQZA==",
            "dev": true
        },
        "vali-date": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/vali-date/-/vali-date-1.0.0.tgz",
            "integrity": "sha1-G5BKWWCfsyjvB4E4Qgk09rhnCaY=",
            "dev": true
        },
        "verror": {
            "version": "1.10.0",
            "resolved": "https://registry.npmjs.org/verror/-/verror-1.10.0.tgz",
            "integrity": "sha1-OhBcoXBTr1XW4nDB+CiGguGNpAA=",
            "dev": true,
            "requires": {
                "assert-plus": "1.0.0",
                "core-util-is": "1.0.2",
                "extsprintf": "1.3.0"
            }
        },
        "vinyl": {
            "version": "0.4.6",
            "resolved": "https://registry.npmjs.org/vinyl/-/vinyl-0.4.6.tgz",
            "integrity": "sha1-LzVsh6VQolVGHza76ypbqL94SEc=",
            "dev": true,
            "requires": {
                "clone": "0.2.0",
                "clone-stats": "0.0.1"
            }
        },
        "vinyl-fs": {
            "version": "2.4.4",
            "resolved": "https://registry.npmjs.org/vinyl-fs/-/vinyl-fs-2.4.4.tgz",
            "integrity": "sha1-vm/zJwy1Xf19MGNkDegfJddTIjk=",
            "dev": true,
            "requires": {
                "duplexify": "3.6.0",
                "glob-stream": "5.3.5",
                "graceful-fs": "4.1.11",
                "gulp-sourcemaps": "1.6.0",
                "is-valid-glob": "0.3.0",
                "lazystream": "1.0.0",
                "lodash.isequal": "4.5.0",
                "merge-stream": "1.0.1",
                "mkdirp": "0.5.1",
                "object-assign": "4.1.1",
                "readable-stream": "2.3.6",
                "strip-bom": "2.0.0",
                "strip-bom-stream": "1.0.0",
                "through2": "2.0.3",
                "through2-filter": "2.0.0",
                "vali-date": "1.0.0",
                "vinyl": "1.2.0"
            },
            "dependencies": {
                "clone": {
                    "version": "1.0.4",
                    "resolved": "https://registry.npmjs.org/clone/-/clone-1.0.4.tgz",
                    "integrity": "sha1-2jCcwmPfFZlMaIypAheco8fNfH4=",
                    "dev": true
                },
                "replace-ext": {
                    "version": "0.0.1",
                    "resolved": "https://registry.npmjs.org/replace-ext/-/replace-ext-0.0.1.tgz",
                    "integrity": "sha1-KbvZIHinOfC8zitO5B6DeVNSKSQ=",
                    "dev": true
                },
                "vinyl": {
                    "version": "1.2.0",
                    "resolved": "https://registry.npmjs.org/vinyl/-/vinyl-1.2.0.tgz",
                    "integrity": "sha1-XIgDbPVl5d8FVYv8kR+GVt8hiIQ=",
                    "dev": true,
                    "requires": {
                        "clone": "1.0.4",
                        "clone-stats": "0.0.1",
                        "replace-ext": "0.0.1"
                    }
                }
            }
        },
        "vinyl-source-stream": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/vinyl-source-stream/-/vinyl-source-stream-1.1.2.tgz",
            "integrity": "sha1-YrU6E1YQqJbpjKlr7jqH8Aio54A=",
            "dev": true,
            "requires": {
                "through2": "2.0.3",
                "vinyl": "0.4.6"
            }
        },
        "vscode": {
            "version": "1.1.21",
            "resolved": "https://registry.npmjs.org/vscode/-/vscode-1.1.21.tgz",
            "integrity": "sha512-tJl9eL15ZMm6vzCYYeQ26sSYRuXGMGPsaeIAmG2rOOYRn01jdaDg6I4b9G5Ed6FISdmn6egpKThk4o4om8Ax/A==",
            "dev": true,
            "requires": {
                "glob": "7.1.3",
                "gulp-chmod": "2.0.0",
                "gulp-filter": "5.1.0",
                "gulp-gunzip": "1.0.0",
                "gulp-remote-src-vscode": "0.5.0",
                "gulp-symdest": "1.1.0",
                "gulp-untar": "0.0.7",
                "gulp-vinyl-zip": "2.1.0",
                "mocha": "4.1.0",
                "request": "2.88.0",
                "semver": "5.5.1",
                "source-map-support": "0.5.9",
                "url-parse": "1.4.3",
                "vinyl-source-stream": "1.1.2"
            }
        },
        "wrappy": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
            "integrity": "sha1-tSQ9jz7BqjXxNkYFvA0QNuMKtp8=",
            "dev": true
        },
        "xtend": {
            "version": "4.0.1",
            "resolved": "https://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz",
            "integrity": "sha1-pcbVMr5lbiPbgg77lDofBJmNY68=",
            "dev": true
        },
        "yauzl": {
            "version": "2.10.0",
            "resolved": "https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz",
            "integrity": "sha1-x+sXyT4RLLEIb6bY5R+wZnt5pfk=",
            "dev": true,
            "requires": {
                "buffer-crc32": "0.2.13",
                "fd-slicer": "1.1.0"
            }
        },
        "yazl": {
            "version": "2.4.3",
            "resolved": "https://registry.npmjs.org/yazl/-/yazl-2.4.3.tgz",
            "integrity": "sha1-7CblzIfVYBud+EMtvdPNLlFzoHE=",
            "dev": true,
            "requires": {
                "buffer-crc32": "0.2.13"
            }
        }
    }
}
'''
saveDefault(filename,text)
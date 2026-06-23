.class public final Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;
.super Landroidx/recyclerview/widget/z1;
.source "r8-map-id-9d1f2360191d13a45a10b49b79fbe48c2fab7f3150b7ece2afb1a52052a3928e"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/anslayer/ui/servers/ServerAdapter;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x19
    name = "ServerHolder"
.end annotation

.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder$WhenMappings;
    }
.end annotation

.annotation runtime Lkotlin/Metadata;
.end annotation

.annotation build Lkotlin/jvm/internal/SourceDebugExtension;
.end annotation


# static fields
.field public static final synthetic r:I


# instance fields
.field public final p:Lcom/anslayer/databinding/AdapterServerItemBinding;

.field public final q:Lcom/anslayer/ui/servers/ServerAdapter;


# direct methods
.method public constructor <init>(Lcom/anslayer/databinding/AdapterServerItemBinding;Lcom/anslayer/ui/servers/ServerAdapter;)V
    .locals 2
    .param p1    # Lcom/anslayer/databinding/AdapterServerItemBinding;
        .annotation build Lorg/jetbrains/annotations/NotNull;
        .end annotation
    .end param
    .param p2    # Lcom/anslayer/ui/servers/ServerAdapter;
        .annotation build Lorg/jetbrains/annotations/NotNull;
        .end annotation
    .end param

    .line 1
    const-string v0, "binding"

    .line 2
    .line 3
    invoke-static {p1, v0}, Lkotlin/jvm/internal/h;->f(Ljava/lang/Object;Ljava/lang/String;)V

    .line 4
    .line 5
    .line 6
    const-string v0, "adapter"

    .line 7
    .line 8
    invoke-static {p2, v0}, Lkotlin/jvm/internal/h;->f(Ljava/lang/Object;Ljava/lang/String;)V

    .line 9
    .line 10
    .line 11
    iget-object v0, p1, Lcom/anslayer/databinding/AdapterServerItemBinding;->a:Landroid/widget/RelativeLayout;

    .line 12
    .line 13
    invoke-direct {p0, v0}, Landroidx/recyclerview/widget/z1;-><init>(Landroid/view/View;)V

    .line 14
    .line 15
    .line 16
    iput-object p1, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->p:Lcom/anslayer/databinding/AdapterServerItemBinding;

    .line 17
    .line 18
    iput-object p2, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->q:Lcom/anslayer/ui/servers/ServerAdapter;

    .line 19
    .line 20
    new-instance p2, Lcom/anslayer/ui/servers/f;

    .line 21
    .line 22
    invoke-direct {p2, p0}, Lcom/anslayer/ui/servers/f;-><init>(Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;)V

    .line 23
    .line 24
    .line 25
    invoke-virtual {v0, p2}, Landroid/view/View;->setOnKeyListener(Landroid/view/View$OnKeyListener;)V

    .line 26
    .line 27
    .line 28
    iget-object p2, p1, Lcom/anslayer/databinding/AdapterServerItemBinding;->choose:Lcom/google/android/material/button/MaterialButton;

    .line 29
    .line 30
    new-instance v0, Lcom/anslayer/ui/servers/e;

    .line 31
    .line 32
    const/4 v1, 0x1

    .line 33
    invoke-direct {v0, p0, v1}, Lcom/anslayer/ui/servers/e;-><init>(Ljava/lang/Object;I)V

    .line 34
    .line 35
    .line 36
    invoke-virtual {p2, v0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 37
    .line 38
    .line 39
    iget-object p1, p1, Lcom/anslayer/databinding/AdapterServerItemBinding;->choose:Lcom/google/android/material/button/MaterialButton;

    .line 40
    .line 41
    const/4 p2, 0x0

    .line 42
    invoke-virtual {p1, p2}, Landroid/view/View;->setFocusable(Z)V

    .line 43
    .line 44
    .line 45
    return-void
    .line 46
    .line 47
    .line 48
    .line 49
    .line 50
    .line 51
    .line 52
    .line 53
    .line 54
    .line 55
    .line 56
    .line 57
    .line 58
    .line 59
    .line 60
    .line 61
    .line 62
    .line 63
    .line 64
    .line 65
    .line 66
    .line 67
    .line 68
    .line 69
    .line 70
    .line 71
    .line 72
    .line 73
    .line 74
    .line 75
    .line 76
    .line 77
    .line 78
    .line 79
    .line 80
    .line 81
    .line 82
    .line 83
    .line 84
    .line 85
    .line 86
    .line 87
    .line 88
    .line 89
    .line 90
    .line 91
    .line 92
    .line 93
    .line 94
    .line 95
    .line 96
    .line 97
    .line 98
    .line 99
    .line 100
    .line 101
    .line 102
    .line 103
    .line 104
    .line 105
    .line 106
    .line 107
    .line 108
    .line 109
    .line 110
    .line 111
    .line 112
    .line 113
    .line 114
    .line 115
    .line 116
    .line 117
    .line 118
    .line 119
    .line 120
    .line 121
    .line 122
    .line 123
    .line 124
    .line 125
    .line 126
    .line 127
    .line 128
    .line 129
    .line 130
    .line 131
    .line 132
    .line 133
    .line 134
    .line 135
    .line 136
    .line 137
    .line 138
    .line 139
    .line 140
    .line 141
    .line 142
    .line 143
    .line 144
    .line 145
    .line 146
    .line 147
    .line 148
    .line 149
    .line 150
    .line 151
    .line 152
    .line 153
    .line 154
    .line 155
    .line 156
    .line 157
    .line 158
    .line 159
    .line 160
    .line 161
    .line 162
    .line 163
    .line 164
    .line 165
    .line 166
    .line 167
    .line 168
    .line 169
    .line 170
    .line 171
    .line 172
    .line 173
    .line 174
    .line 175
    .line 176
    .line 177
    .line 178
    .line 179
    .line 180
    .line 181
    .line 182
    .line 183
    .line 184
.end method


# virtual methods
.method public final a()V
    .locals 7

    .line 1
    invoke-virtual {p0}, Landroidx/recyclerview/widget/z1;->getBindingAdapterPosition()I

    .line 2
    .line 3
    .line 4
    move-result v0

    .line 5
    const/4 v1, -0x1

    .line 6
    if-ne v0, v1, :cond_0

    .line 7
    .line 8
    goto :goto_0

    .line 9
    :cond_0
    invoke-virtual {p0}, Landroidx/recyclerview/widget/z1;->getBindingAdapterPosition()I

    .line 10
    .line 11
    .line 12
    move-result v0

    .line 13
    iget-object v1, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->q:Lcom/anslayer/ui/servers/ServerAdapter;

    .line 14
    .line 15
    invoke-virtual {v1, v0}, Landroidx/recyclerview/widget/s0;->getItem(I)Ljava/lang/Object;

    .line 16
    .line 17
    .line 18
    move-result-object v0

    .line 19
    check-cast v0, Lv3/r0;

    .line 20
    .line 21
    if-nez v0, :cond_1

    .line 22
    .line 23
    goto :goto_0

    .line 24
    :cond_1
    iget-boolean v2, v0, Lv3/r0;->j:Z

    .line 25
    .line 26
    if-nez v2, :cond_2

    .line 27
    .line 28
    :goto_0
    return-void

    .line 29
    :cond_2
    iget-object v2, v1, Lcom/anslayer/ui/servers/ServerAdapter;->r:Ljava/util/List;

    .line 30
    .line 31
    invoke-interface {v2}, Ljava/lang/Iterable;->iterator()Ljava/util/Iterator;

    .line 32
    .line 33
    .line 34
    move-result-object v2

    .line 35
    :cond_3
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    .line 36
    .line 37
    .line 38
    move-result v3

    .line 39
    if-eqz v3, :cond_4

    .line 40
    .line 41
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    .line 42
    .line 43
    .line 44
    move-result-object v3

    .line 45
    move-object v4, v3

    .line 46
    check-cast v4, Lcom/anslayer/model/resolver/ServersModel;

    .line 47
    .line 48
    iget-object v5, v0, Lv3/r0;->a:Ljava/lang/String;

    .line 49
    .line 50
    invoke-virtual {v4}, Lcom/anslayer/model/resolver/ServersModel;->getName()Ljava/lang/String;

    .line 51
    .line 52
    .line 53
    move-result-object v4

    .line 54
    const/4 v6, 0x0

    .line 55
    invoke-static {v5, v4, v6}, Lkotlin/text/i;->G(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Z)Z

    .line 56
    .line 57
    .line 58
    move-result v4

    .line 59
    if-eqz v4, :cond_3

    .line 60
    .line 61
    goto :goto_1

    .line 62
    :cond_4
    const/4 v3, 0x0

    .line 63
    :goto_1
    check-cast v3, Lcom/anslayer/model/resolver/ServersModel;

    .line 64
    .line 65
    iget-object v2, v1, Lcom/anslayer/ui/servers/ServerAdapter;->q:Lcom/anslayer/ui/servers/ServerAdapter$OnServerItemClickListener;

    .line 66
    .line 67
    iget-object v1, v1, Lcom/anslayer/ui/servers/ServerAdapter;->s:Ljava/lang/String;

    .line 68
    .line 69
    invoke-virtual {p0}, Landroidx/recyclerview/widget/z1;->getBindingAdapterPosition()I

    .line 70
    .line 71
    .line 72
    move-result v4

    .line 73
    invoke-interface {v2, v3, v1, v4, v0}, Lcom/anslayer/ui/servers/ServerAdapter$OnServerItemClickListener;->onServerItemClick(Lcom/anslayer/model/resolver/ServersModel;Ljava/lang/String;ILv3/r0;)V

    .line 74
    .line 75
    .line 76
    return-void
    .line 77
    .line 78
    .line 79
    .line 80
    .line 81
    .line 82
    .line 83
    .line 84
    .line 85
    .line 86
    .line 87
    .line 88
    .line 89
    .line 90
    .line 91
    .line 92
    .line 93
    .line 94
    .line 95
    .line 96
    .line 97
    .line 98
    .line 99
    .line 100
    .line 101
    .line 102
    .line 103
    .line 104
    .line 105
    .line 106
    .line 107
    .line 108
    .line 109
    .line 110
    .line 111
    .line 112
    .line 113
    .line 114
    .line 115
    .line 116
    .line 117
    .line 118
    .line 119
    .line 120
    .line 121
    .line 122
    .line 123
    .line 124
    .line 125
    .line 126
    .line 127
    .line 128
    .line 129
    .line 130
    .line 131
    .line 132
    .line 133
    .line 134
    .line 135
    .line 136
    .line 137
    .line 138
    .line 139
    .line 140
    .line 141
    .line 142
    .line 143
    .line 144
    .line 145
    .line 146
    .line 147
    .line 148
    .line 149
    .line 150
    .line 151
    .line 152
    .line 153
    .line 154
    .line 155
    .line 156
    .line 157
    .line 158
    .line 159
    .line 160
    .line 161
    .line 162
    .line 163
    .line 164
    .line 165
    .line 166
    .line 167
    .line 168
    .line 169
    .line 170
    .line 171
    .line 172
    .line 173
    .line 174
    .line 175
    .line 176
    .line 177
    .line 178
    .line 179
    .line 180
    .line 181
    .line 182
    .line 183
    .line 184
    .line 185
    .line 186
    .line 187
    .line 188
    .line 189
    .line 190
    .line 191
    .line 192
    .line 193
    .line 194
    .line 195
    .line 196
    .line 197
    .line 198
    .line 199
    .line 200
    .line 201
    .line 202
    .line 203
    .line 204
    .line 205
    .line 206
    .line 207
    .line 208
    .line 209
    .line 210
    .line 211
    .line 212
    .line 213
    .line 214
    .line 215
    .line 216
    .line 217
    .line 218
    .line 219
    .line 220
    .line 221
    .line 222
    .line 223
    .line 224
    .line 225
    .line 226
    .line 227
    .line 228
    .line 229
.end method

.method public final bind(Lv3/r0;)V
    .locals 3
    .param p1    # Lv3/r0;
        .annotation build Lorg/jetbrains/annotations/NotNull;
        .end annotation
    .end param

    .line 1
    const-string v0, "server"

    .line 2
    .line 3
    invoke-static {p1, v0}, Lkotlin/jvm/internal/h;->f(Ljava/lang/Object;Ljava/lang/String;)V

    .line 4
    .line 5
    .line 6
    .line 6
    iget-boolean v0, p1, Lv3/r0;->g:Z
    if-eqz v0, :force_enable_skip
    const/4 v0, 0x1
    iput-boolean v0, p1, Lv3/r0;->j:Z
    sget-object v0, Lv3/t0;->r:Lv3/t0;
    iput-object v0, p1, Lv3/r0;->h:Lv3/t0;
    :force_enable_skip
    iget-boolean v0, p1, Lv3/r0;->j:Z

    .line 7
    .line 8
    invoke-virtual {p0, v0}, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->setServerEnabled(Z)V

    .line 9
    .line 10
    .line 11
    iget-object v0, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->p:Lcom/anslayer/databinding/AdapterServerItemBinding;

    .line 12
    .line 13
    iget-object v1, v0, Lcom/anslayer/databinding/AdapterServerItemBinding;->serverName:Landroid/widget/TextView;

    .line 14
    .line 15
    iget-object v2, p1, Lv3/r0;->c:Ljava/lang/String;

    .line 16
    .line 17
    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 18
    .line 19
    .line 20
    iget-boolean v1, p1, Lv3/r0;->g:Z

    .line 21
    .line 22
    iget-object v2, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->q:Lcom/anslayer/ui/servers/ServerAdapter;

    .line 23
    .line 24
    if-eqz v1, :cond_0

    .line 25
    .line 26
    iget-object p1, v0, Lcom/anslayer/databinding/AdapterServerItemBinding;->serverName:Landroid/widget/TextView;

    .line 27
    .line 28
    iget v1, v2, Lcom/anslayer/ui/servers/ServerAdapter;->u:I

    .line 29
    .line 30
    invoke-virtual {p1, v1}, Landroid/widget/TextView;->setTextColor(I)V

    .line 31
    .line 32
    .line 33
    iget-object p1, v0, Lcom/anslayer/databinding/AdapterServerItemBinding;->serverState:Landroid/widget/ImageView;

    .line 34
    .line 35
    sget v0, Lcom/anslayer/R$drawable;->ic_radio_button_checked_green_600_24dp:I

    .line 36
    .line 37
    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 38
    .line 39
    .line 40
    return-void

    .line 41
    :cond_0
    iget-object v0, v0, Lcom/anslayer/databinding/AdapterServerItemBinding;->serverName:Landroid/widget/TextView;

    .line 42
    .line 43
    iget v1, v2, Lcom/anslayer/ui/servers/ServerAdapter;->t:I

    .line 44
    .line 45
    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setTextColor(I)V

    .line 46
    .line 47
    .line 48
    invoke-virtual {p0, p1}, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->setServerState(Lv3/r0;)V

    .line 49
    .line 50
    .line 51
    return-void
    .line 52
    .line 53
    .line 54
    .line 55
    .line 56
    .line 57
    .line 58
    .line 59
    .line 60
    .line 61
    .line 62
    .line 63
    .line 64
    .line 65
    .line 66
    .line 67
    .line 68
    .line 69
    .line 70
    .line 71
.end method

.method public final setServerEnabled(Z)V
    .locals 1

    .line 1
    iget-object v0, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->p:Lcom/anslayer/databinding/AdapterServerItemBinding;

    .line 2
    .line 3
    iget-object v0, v0, Lcom/anslayer/databinding/AdapterServerItemBinding;->choose:Lcom/google/android/material/button/MaterialButton;

    .line 4
    .line 5
    invoke-virtual {v0, p1}, Landroid/view/View;->setEnabled(Z)V

    .line 6
    .line 7
    .line 8
    if-eqz p1, :cond_0

    .line 9
    .line 10
    const/high16 p1, 0x3f800000    # 1.0f

    .line 11
    .line 12
    goto :goto_0

    .line 13
    :cond_0
    const/high16 p1, 0x3f000000    # 0.5f

    .line 14
    .line 15
    :goto_0
    invoke-virtual {v0, p1}, Landroid/view/View;->setAlpha(F)V

    .line 16
    .line 17
    .line 18
    return-void
    .line 19
    .line 20
    .line 21
    .line 22
    .line 23
    .line 24
.end method

.method public final setServerState(Lv3/r0;)V
    .locals 1
    .param p1    # Lv3/r0;
        .annotation build Lorg/jetbrains/annotations/NotNull;
        .end annotation
    .end param

    .line 1
    const-string v0, "server"

    .line 2
    .line 3
    invoke-static {p1, v0}, Lkotlin/jvm/internal/h;->f(Ljava/lang/Object;Ljava/lang/String;)V

    .line 4
    .line 5
    .line 6
    iget-object p1, p1, Lv3/r0;->h:Lv3/t0;

    .line 7
    .line 8
    sget-object v0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder$WhenMappings;->$EnumSwitchMapping$0:[I

    .line 9
    .line 10
    invoke-virtual {p1}, Ljava/lang/Enum;->ordinal()I

    .line 11
    .line 12
    .line 13
    move-result p1

    .line 14
    aget p1, v0, p1

    .line 15
    .line 16
    const/4 v0, 0x1

    .line 17
    if-eq p1, v0, :cond_2

    .line 18
    .line 19
    const/4 v0, 0x2

    .line 20
    if-eq p1, v0, :cond_1

    .line 21
    .line 22
    const/4 v0, 0x3

    .line 23
    if-ne p1, v0, :cond_0

    .line 24
    .line 25
    sget p1, Lcom/anslayer/R$drawable;->ic_radio_button_checked_red_600_24dp:I

    .line 26
    .line 27
    goto :goto_0

    .line 28
    :cond_0
    new-instance p1, Lkotlin/NoWhenBranchMatchedException;

    .line 29
    .line 30
    invoke-direct {p1}, Lkotlin/NoWhenBranchMatchedException;-><init>()V

    .line 31
    .line 32
    .line 33
    throw p1

    .line 34
    :cond_1
    sget p1, Lcom/anslayer/R$drawable;->ic_radio_button_checked_green_600_24dp:I

    .line 35
    .line 36
    goto :goto_0

    .line 37
    :cond_2
    sget p1, Lcom/anslayer/R$drawable;->ic_info_outline_orange_600_24dp:I

    .line 38
    .line 39
    :goto_0
    iget-object v0, p0, Lcom/anslayer/ui/servers/ServerAdapter$ServerHolder;->p:Lcom/anslayer/databinding/AdapterServerItemBinding;

    .line 40
    .line 41
    iget-object v0, v0, Lcom/anslayer/databinding/AdapterServerItemBinding;->serverState:Landroid/widget/ImageView;

    .line 42
    .line 43
    invoke-virtual {v0, p1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 44
    .line 45
    .line 46
    return-void
    .line 47
    .line 48
    .line 49
    .line 50
    .line 51
    .line 52
    .line 53
    .line 54
    .line 55
    .line 56
    .line 57
    .line 58
    .line 59
    .line 60
    .line 61
    .line 62
    .line 63
    .line 64
    .line 65
    .line 66
    .line 67
    .line 68
    .line 69
    .line 70
    .line 71
.end method

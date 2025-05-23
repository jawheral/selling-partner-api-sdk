/*
 * Selling Partner API for Finances
 * The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order, financial event group, or date range without having to wait until a statement period closes. You can also obtain financial event groups for a given date range.
 *
 * OpenAPI spec version: v0
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.finances.v0;

import com.google.gson.annotations.SerializedName;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.Objects;
import org.threeten.bp.OffsetDateTime;

/** An event related to an Adhoc Disbursement. */
@Schema(description = "An event related to an Adhoc Disbursement.")
public class AdhocDisbursementEvent {
    @SerializedName("TransactionType")
    private String transactionType = null;

    @SerializedName("PostedDate")
    private OffsetDateTime postedDate = null;

    @SerializedName("TransactionId")
    private String transactionId = null;

    @SerializedName("TransactionAmount")
    private Currency transactionAmount = null;

    public AdhocDisbursementEvent transactionType(String transactionType) {
        this.transactionType = transactionType;
        return this;
    }

    /**
     * Indicates the type of transaction. Example: \&quot;Disbursed to Amazon Gift Card balance\&quot;
     *
     * @return transactionType
     */
    @Schema(description = "Indicates the type of transaction.  Example: \"Disbursed to Amazon Gift Card balance\"")
    public String getTransactionType() {
        return transactionType;
    }

    public void setTransactionType(String transactionType) {
        this.transactionType = transactionType;
    }

    public AdhocDisbursementEvent postedDate(OffsetDateTime postedDate) {
        this.postedDate = postedDate;
        return this;
    }

    /**
     * Get postedDate
     *
     * @return postedDate
     */
    @Schema(description = "")
    public OffsetDateTime getPostedDate() {
        return postedDate;
    }

    public void setPostedDate(OffsetDateTime postedDate) {
        this.postedDate = postedDate;
    }

    public AdhocDisbursementEvent transactionId(String transactionId) {
        this.transactionId = transactionId;
        return this;
    }

    /**
     * The identifier for the transaction.
     *
     * @return transactionId
     */
    @Schema(description = "The identifier for the transaction.")
    public String getTransactionId() {
        return transactionId;
    }

    public void setTransactionId(String transactionId) {
        this.transactionId = transactionId;
    }

    public AdhocDisbursementEvent transactionAmount(Currency transactionAmount) {
        this.transactionAmount = transactionAmount;
        return this;
    }

    /**
     * Get transactionAmount
     *
     * @return transactionAmount
     */
    @Schema(description = "")
    public Currency getTransactionAmount() {
        return transactionAmount;
    }

    public void setTransactionAmount(Currency transactionAmount) {
        this.transactionAmount = transactionAmount;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        AdhocDisbursementEvent adhocDisbursementEvent = (AdhocDisbursementEvent) o;
        return Objects.equals(this.transactionType, adhocDisbursementEvent.transactionType)
                && Objects.equals(this.postedDate, adhocDisbursementEvent.postedDate)
                && Objects.equals(this.transactionId, adhocDisbursementEvent.transactionId)
                && Objects.equals(this.transactionAmount, adhocDisbursementEvent.transactionAmount);
    }

    @Override
    public int hashCode() {
        return Objects.hash(transactionType, postedDate, transactionId, transactionAmount);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class AdhocDisbursementEvent {\n");

        sb.append("    transactionType: ")
                .append(toIndentedString(transactionType))
                .append("\n");
        sb.append("    postedDate: ").append(toIndentedString(postedDate)).append("\n");
        sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
        sb.append("    transactionAmount: ")
                .append(toIndentedString(transactionAmount))
                .append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
